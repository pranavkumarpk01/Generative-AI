"""
Configuration module for GitHub API Demo
Handles environment variables and constants
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# GitHub API Configuration
GITHUB_API_BASE_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_REPO = os.getenv("GITHUB_REPO")

# Validate that required environment variables are set
def validate_config():
    """Validate that all required configuration is present"""
    missing = []
    
    if not GITHUB_TOKEN:
        missing.append("GITHUB_TOKEN")
    if not GITHUB_USERNAME:
        missing.append("GITHUB_USERNAME")
    if not GITHUB_REPO:
        missing.append("GITHUB_REPO")
    
    if missing:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing)}\n"
            f"Please create a .env file with these variables."
        )

# API Endpoints
ENDPOINTS = {
    "user": "/user",
    "repos": "/user/repos",
    "repo_detail": "/repos/{owner}/{repo}",
    "issues": "/repos/{owner}/{repo}/issues",
    "issue_detail": "/repos/{owner}/{repo}/issues/{issue_number}",
    "pulls": "/repos/{owner}/{repo}/pulls",
    "pull_detail": "/repos/{owner}/{repo}/pulls/{pull_number}",
}

# Sample data for testing
SAMPLE_ISSUE = {
    "title": "Update documentation with API examples",
    "body": "The README needs more practical examples for API integration.",
    "labels": ["documentation", "enhancement"],
}

SAMPLE_ISSUE_UPDATE = {
    "title": "Update documentation with API examples (UPDATED)",
    "body": "The README needs more practical examples for API integration. Status: In Progress",
    "state": "open",
}

# HTTP Headers
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "GitHub-API-Demo-Python",
}

# Logging configuration
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_LEVEL = "INFO"
