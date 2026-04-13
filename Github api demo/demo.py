"""
GitHub API CRUD Demo
Demonstrates Create, Read, Update, Delete operations
"""

import json
import time
from github_api_client import GitHubAPIClient
from config import SAMPLE_ISSUE, SAMPLE_ISSUE_UPDATE


def print_section(title: str) -> None:
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def print_success(message: str) -> None:
    """Print success message"""
    print(f"  ✓ {message}")


def print_error(message: str) -> None:
    """Print error message"""
    print(f"  ✗ {message}")


def print_data(data: dict, indent: int = 2) -> None:
    """Pretty print JSON data"""
    spaces = " " * indent
    print(json.dumps(data, indent=indent)[:500] + "...")


def demo_authentication(client: GitHubAPIClient) -> bool:
    """Verify authentication works"""
    print_section("STEP 1: Verify Authentication")
    success, user_data = client.get_user_info()

    if success:
        print_success(f"Authenticated as: {user_data.get('login')}")
        print(f"  Name: {user_data.get('name')}")
        print(f"  Public repos: {user_data.get('public_repos')}")
        return True
    else:
        print_error(f"Authentication failed: {user_data.get('error')}")
        return False


def demo_repository_info(client: GitHubAPIClient) -> bool:
    """Get repository information"""
    print_section("STEP 2: Get Repository Information")
    success, repo_data = client.get_repository_info()

    if success:
        print_success(f"Repository: {repo_data.get('full_name')}")
        print(f"  Description: {repo_data.get('description', 'N/A')}")
        print(f"  Stars: {repo_data.get('stargazers_count')}")
        print(f"  Language: {repo_data.get('language', 'N/A')}")
        print(f"  Visibility: {repo_data.get('private') and 'Private' or 'Public'}")
        return True
    else:
        print_error(f"Failed to get repo info: {repo_data.get('error')}")
        return False


def demo_create_issue(client: GitHubAPIClient) -> dict:
    """CREATE: Create a new issue"""
    print_section("STEP 3: CREATE - Create a New Issue")
    print(f"  Issue title: {SAMPLE_ISSUE['title']}")
    print(f"  Labels: {SAMPLE_ISSUE['labels']}")

    success, response = client.create_issue(
        title=SAMPLE_ISSUE["title"],
        body=SAMPLE_ISSUE["body"],
        labels=SAMPLE_ISSUE["labels"],
    )

    if success:
        issue_number = response.get("number")
        print_success(f"Issue created with number: #{issue_number}")
        client.print_issue(response)
        return {"success": True, "number": issue_number, "data": response}
    else:
        print_error(f"Failed to create issue: {response.get('error')}")
        return {"success": False}


def demo_read_issue(client: GitHubAPIClient, issue_number: int) -> dict:
    """READ: Get a specific issue"""
    print_section("STEP 4: READ - Retrieve Specific Issue")
    print(f"  Fetching issue #{issue_number}...")

    success, response = client.get_issue(issue_number)

    if success:
        print_success(f"Issue retrieved successfully")
        client.print_issue(response)
        return {"success": True, "data": response}
    else:
        print_error(f"Failed to read issue: {response.get('error')}")
        return {"success": False}


def demo_update_issue(client: GitHubAPIClient, issue_number: int) -> dict:
    """UPDATE: Update an existing issue"""
    print_section("STEP 5: UPDATE - Modify the Issue")
    print(f"  Updating issue #{issue_number}...")
    print(f"  New title: {SAMPLE_ISSUE_UPDATE['title']}")

    success, response = client.update_issue(
        issue_number,
        title=SAMPLE_ISSUE_UPDATE["title"],
        body=SAMPLE_ISSUE_UPDATE["body"],
    )

    if success:
        print_success(f"Issue updated successfully")
        client.print_issue(response)
        return {"success": True, "data": response}
    else:
        print_error(f"Failed to update issue: {response.get('error')}")
        return {"success": False}


def demo_list_issues(client: GitHubAPIClient) -> dict:
    """READ: List all issues"""
    print_section("STEP 6: READ - List All Issues")
    print(f"  Fetching all issues...")

    success, issues = client.list_issues(state="all")

    if success:
        print_success(f"Retrieved {len(issues)} issue(s)")
        if issues:
            for issue in issues[:5]:  # Show first 5
                print(f"    • #{issue.get('number')}: {issue.get('title')} ({issue.get('state')})")
            if len(issues) > 5:
                print(f"    ... and {len(issues) - 5} more")
        return {"success": True, "count": len(issues), "data": issues}
    else:
        print_error(f"Failed to list issues: {issues}")
        return {"success": False}


def demo_delete_issue(client: GitHubAPIClient, issue_number: int) -> dict:
    """DELETE: Close an issue"""
    print_section("STEP 7: DELETE - Close the Issue")
    print(f"  Closing issue #{issue_number}...")

    success, response = client.update_issue(issue_number, state="closed")

    if success:
        print_success(f"Issue #{issue_number} closed successfully")
        print(f"  State: {response.get('state')}")
        return {"success": True, "data": response}
    else:
        print_error(f"Failed to delete issue: {response.get('error')}")
        return {"success": False}


def demo_pull_requests(client: GitHubAPIClient) -> None:
    """Demonstrate PR operations"""
    print_section("STEP 8: Pull Request Operations")
    print("  Note: Creating a PR requires an existing branch.")
    print("  For demonstration, we'll just list existing PRs.\n")

    success, prs = client.list_pull_requests()

    if success:
        print_success(f"Retrieved {len(prs)} PR(s)")
        if prs:
            for pr in prs[:3]:
                print(f"    • #{pr.get('number')}: {pr.get('title')} ({pr.get('state')})")
        else:
            print("  (No pull requests found)")
    else:
        print_error(f"Failed to list PRs: {prs}")


def print_summary(results: dict) -> None:
    """Print a summary of all operations"""
    print_section("DEMO SUMMARY")
    print("\n  Operations Performed:")
    print(f"    ✓ Authentication: Verified")
    print(f"    ✓ Repository Info: Retrieved")
    print(f"    ✓ Create Issue: {results['create'].get('success') and 'Success' or 'Failed'}")
    print(f"    ✓ Read Issue: {results['read'].get('success') and 'Success' or 'Failed'}")
    print(f"    ✓ Update Issue: {results['update'].get('success') and 'Success' or 'Failed'}")
    print(f"    ✓ List Issues: {results['list'].get('success') and 'Success' or 'Failed'}")
    print(f"    ✓ Delete Issue: {results['delete'].get('success') and 'Success' or 'Failed'}")

    total_issues = results["list"].get("count", 0)
    print(f"\n  Repository Statistics:")
    print(f"    Total issues: {total_issues}")

    print(f"\n  Next Steps:")
    print(f"    1. Modify the sample data in config.py")
    print(f"    2. Add more operations (comments, reactions, etc.)")
    print(f"    3. Integrate with a database to store results")
    print(f"    4. Build a web dashboard with the API data")


def main():
    """Main demo execution"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  GitHub API CRUD Demo - Full Tutorial".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")

    # Initialize client
    try:
        client = GitHubAPIClient()
    except ValueError as e:
        print(f"\n✗ Configuration Error: {str(e)}")
        return

    results = {}

    # Step 1: Verify authentication
    if not demo_authentication(client):
        print_error("Authentication failed. Please check your token.")
        return

    # Step 2: Get repo info
    demo_repository_info(client)

    # Step 3: CREATE an issue
    create_result = demo_create_issue(client)
    results["create"] = create_result

    if not create_result.get("success"):
        print_error("Cannot continue without creating an issue first.")
        return

    issue_number = create_result["number"]
    time.sleep(1)  # Brief pause to avoid rate limiting

    # Step 4: READ the issue
    results["read"] = demo_read_issue(client, issue_number)
    time.sleep(1)

    # Step 5: UPDATE the issue
    results["update"] = demo_update_issue(client, issue_number)
    time.sleep(1)

    # Step 6: LIST all issues
    results["list"] = demo_list_issues(client)
    time.sleep(1)

    # Step 7: DELETE the issue
    results["delete"] = demo_delete_issue(client, issue_number)
    time.sleep(1)

    # Step 8: Pull request operations
    demo_pull_requests(client)

    # Print summary
    print_summary(results)

    print("\n✓ Demo completed successfully!\n")


if __name__ == "__main__":
    main()
