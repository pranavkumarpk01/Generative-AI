"""
GitHub API Client
Handles all CRUD operations with error handling and logging
"""

import requests
import json
import logging
from typing import Dict, List, Optional, Tuple
from config import (
    GITHUB_API_BASE_URL,
    GITHUB_TOKEN,
    GITHUB_USERNAME,
    GITHUB_REPO,
    HEADERS,
    validate_config,
)

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class GitHubAPIClient:
    """
    Client for interacting with GitHub REST API
    Supports CRUD operations on issues and pull requests
    """

    def __init__(self):
        """Initialize the GitHub API client"""
        validate_config()
        self.base_url = GITHUB_API_BASE_URL
        self.token = GITHUB_TOKEN
        self.username = GITHUB_USERNAME
        self.repo = GITHUB_REPO
        self.headers = HEADERS.copy()
        self.headers["Authorization"] = f"token {self.token}"

    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None,
    ) -> Tuple[bool, Dict]:
        """
        Make an HTTP request to GitHub API

        Args:
            method: HTTP method (GET, POST, PATCH, DELETE)
            endpoint: API endpoint path
            data: Request body data
            params: Query parameters

        Returns:
            Tuple of (success: bool, response: dict)
        """
        url = f"{self.base_url}{endpoint}"

        try:
            logger.info(f"{method} {url}")

            if method == "GET":
                response = requests.get(url, headers=self.headers, params=params)
            elif method == "POST":
                response = requests.post(url, headers=self.headers, json=data)
            elif method == "PATCH":
                response = requests.patch(url, headers=self.headers, json=data)
            elif method == "DELETE":
                response = requests.delete(url, headers=self.headers)
            else:
                logger.error(f"Unsupported HTTP method: {method}")
                return False, {"error": f"Unsupported method: {method}"}

            # Handle different status codes
            if response.status_code == 204:  # No content (successful delete)
                return True, {"message": "Successfully deleted"}
            elif response.status_code in [200, 201]:  # Success
                return True, response.json()
            elif response.status_code == 401:
                logger.error("Authentication failed: Invalid token")
                return False, {"error": "Authentication failed: Invalid token"}
            elif response.status_code == 403:
                logger.error("Rate limit exceeded or access forbidden")
                return False, {"error": "Rate limit exceeded or forbidden"}
            elif response.status_code == 404:
                logger.error(f"Resource not found: {endpoint}")
                return False, {"error": "Resource not found"}
            elif response.status_code == 422:
                logger.error(f"Validation failed: {response.text}")
                return False, response.json()
            else:
                logger.error(f"Unexpected status code: {response.status_code}")
                return False, {"error": f"HTTP {response.status_code}: {response.text}"}

        except requests.exceptions.ConnectionError:
            logger.error("Connection error: Unable to reach GitHub API")
            return False, {"error": "Connection error"}
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return False, {"error": str(e)}

    # ==================== ISSUE OPERATIONS ====================

    def create_issue(self, title: str, body: str = "", labels: Optional[List[str]] = None) -> Tuple[bool, Dict]:
        """
        CREATE: Create a new issue

        Args:
            title: Issue title
            body: Issue description
            labels: List of labels

        Returns:
            Tuple of (success: bool, response: dict)
        """
        endpoint = f"/repos/{self.username}/{self.repo}/issues"
        data = {"title": title, "body": body}
        if labels:
            data["labels"] = labels

        success, response = self._make_request("POST", endpoint, data)
        if success:
            logger.info(f"✓ Issue created: #{response.get('number')} - {response.get('title')}")
        return success, response

    def get_issue(self, issue_number: int) -> Tuple[bool, Dict]:
        """
        READ: Get a specific issue

        Args:
            issue_number: Issue number

        Returns:
            Tuple of (success: bool, response: dict)
        """
        endpoint = f"/repos/{self.username}/{self.repo}/issues/{issue_number}"
        success, response = self._make_request("GET", endpoint)
        if success:
            logger.info(f"✓ Issue #{issue_number} retrieved")
        return success, response

    def list_issues(self, state: str = "all", labels: Optional[str] = None) -> Tuple[bool, List[Dict]]:
        """
        READ: List all issues

        Args:
            state: Issue state (open, closed, all)
            labels: Comma-separated labels to filter by

        Returns:
            Tuple of (success: bool, issues: list)
        """
        endpoint = f"/repos/{self.username}/{self.repo}/issues"
        params = {"state": state, "per_page": 100}
        if labels:
            params["labels"] = labels

        success, response = self._make_request("GET", endpoint, params=params)
        if success:
            logger.info(f"✓ Retrieved {len(response)} issue(s)")
        return success, response if success else []

    def update_issue(
        self, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None
    ) -> Tuple[bool, Dict]:
        """
        UPDATE: Update an existing issue

        Args:
            issue_number: Issue number
            title: New title
            body: New body
            state: New state (open, closed)

        Returns:
            Tuple of (success: bool, response: dict)
        """
        endpoint = f"/repos/{self.username}/{self.repo}/issues/{issue_number}"
        data = {}
        if title is not None:
            data["title"] = title
        if body is not None:
            data["body"] = body
        if state is not None:
            data["state"] = state

        success, response = self._make_request("PATCH", endpoint, data)
        if success:
            logger.info(f"✓ Issue #{issue_number} updated")
        return success, response

    def delete_issue(self, issue_number: int) -> Tuple[bool, Dict]:
        """
        DELETE: Delete an issue (by closing it, as GitHub API doesn't truly delete)

        Args:
            issue_number: Issue number

        Returns:
            Tuple of (success: bool, response: dict)
        """
        # GitHub doesn't support true deletion of issues, so we close them
        return self.update_issue(issue_number, state="closed")

    # ==================== PULL REQUEST OPERATIONS ====================

    def create_pull_request(
        self, title: str, head: str, base: str = "main", body: str = ""
    ) -> Tuple[bool, Dict]:
        """
        CREATE: Create a new pull request

        Args:
            title: PR title
            head: Branch with changes
            base: Base branch (default: main)
            body: PR description

        Returns:
            Tuple of (success: bool, response: dict)
        """
        endpoint = f"/repos/{self.username}/{self.repo}/pulls"
        data = {"title": title, "head": head, "base": base, "body": body}

        success, response = self._make_request("POST", endpoint, data)
        if success:
            logger.info(f"✓ PR created: #{response.get('number')} - {response.get('title')}")
        return success, response

    def get_pull_request(self, pr_number: int) -> Tuple[bool, Dict]:
        """
        READ: Get a specific pull request

        Args:
            pr_number: Pull request number

        Returns:
            Tuple of (success: bool, response: dict)
        """
        endpoint = f"/repos/{self.username}/{self.repo}/pulls/{pr_number}"
        success, response = self._make_request("GET", endpoint)
        if success:
            logger.info(f"✓ PR #{pr_number} retrieved")
        return success, response

    def list_pull_requests(self, state: str = "open") -> Tuple[bool, List[Dict]]:
        """
        READ: List pull requests

        Args:
            state: PR state (open, closed, all)

        Returns:
            Tuple of (success: bool, prs: list)
        """
        endpoint = f"/repos/{self.username}/{self.repo}/pulls"
        params = {"state": state, "per_page": 100}

        success, response = self._make_request("GET", endpoint, params=params)
        if success:
            logger.info(f"✓ Retrieved {len(response)} PR(s)")
        return success, response if success else []

    def update_pull_request(
        self, pr_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None
    ) -> Tuple[bool, Dict]:
        """
        UPDATE: Update a pull request

        Args:
            pr_number: PR number
            title: New title
            body: New body
            state: New state (open, closed)

        Returns:
            Tuple of (success: bool, response: dict)
        """
        endpoint = f"/repos/{self.username}/{self.repo}/pulls/{pr_number}"
        data = {}
        if title is not None:
            data["title"] = title
        if body is not None:
            data["body"] = body
        if state is not None:
            data["state"] = state

        success, response = self._make_request("PATCH", endpoint, data)
        if success:
            logger.info(f"✓ PR #{pr_number} updated")
        return success, response

    # ==================== REPOSITORY OPERATIONS ====================

    def get_repository_info(self) -> Tuple[bool, Dict]:
        """
        READ: Get repository information

        Returns:
            Tuple of (success: bool, response: dict)
        """
        endpoint = f"/repos/{self.username}/{self.repo}"
        success, response = self._make_request("GET", endpoint)
        if success:
            logger.info(f"✓ Repository info retrieved")
        return success, response

    def get_user_info(self) -> Tuple[bool, Dict]:
        """
        READ: Get authenticated user information

        Returns:
            Tuple of (success: bool, response: dict)
        """
        endpoint = "/user"
        success, response = self._make_request("GET", endpoint)
        if success:
            logger.info(f"✓ User info retrieved")
        return success, response

    # ==================== HELPER METHODS ====================

    def print_issue(self, issue: Dict) -> None:
        """Pretty print issue details"""
        print(f"\n  Issue #{issue.get('number')}: {issue.get('title')}")
        print(f"  State: {issue.get('state')}")
        print(f"  Created: {issue.get('created_at')}")
        print(f"  Updated: {issue.get('updated_at')}")
        print(f"  Body: {issue.get('body', 'N/A')[:100]}...")

    def print_pull_request(self, pr: Dict) -> None:
        """Pretty print pull request details"""
        print(f"\n  PR #{pr.get('number')}: {pr.get('title')}")
        print(f"  State: {pr.get('state')}")
        print(f"  Head: {pr.get('head', {}).get('ref')}")
        print(f"  Base: {pr.get('base', {}).get('ref')}")
        print(f"  Created: {pr.get('created_at')}")
