# GitHub API CRUD Demo - Complete Guide

## Overview

This project demonstrates how to interact with GitHub's REST API using Python to perform **CRUD operations** (Create, Read, Update, Delete) on issues and pull requests.

### What You'll Learn
- Authentication with GitHub API
- Making HTTP requests (GET, POST, PATCH, DELETE)
- Handling API responses and errors
- Full CRUD operations
- Best practices for API integration
- Rate limiting and error handling

---

## Project Structure

```
github-api-demo/
├── .env                          # Configuration (Never commit!)
├── .env.example                  # Template for .env
├── .gitignore                    # Git ignore rules
├── config.py                     # Configuration constants
├── github_api_client.py          # Main API client class
├── demo.py                       # Main demonstration script
├── requirements.txt              # Python dependencies
└── GITHUB_API_DEMO_GUIDE.md     # Detailed guide
```

---

## Prerequisites

- Python 3.7+
- GitHub account
- GitHub Personal Access Token

---

## Step-by-Step Setup

### 1. Create a Test Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `demo-repo`
3. Description: `Test repository for API demo`
4. Choose visibility (Public or Private - both work)
5. **Don't** initialize with README, .gitignore, or license
6. Click "Create repository"

### 2. Generate GitHub Personal Access Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. **Token name:** `API Demo Token`
4. **Expiration:** 90 days
5. **Select scopes:**
   - ✓ `repo` (Full control of private repositories)
   - ✓ `admin:repo_hook` (Write access to hooks)
   - ✓ `user` (Read user profile data)
6. Click "Generate token"
7. **Copy the token immediately** (You won't see it again!)

### 3. Clone or Create Project

Option A - Using git:
```bash
git clone <repository-url>
cd github-api-demo
```

Option B - Manual setup:
```bash
mkdir github-api-demo
cd github-api-demo
# Copy the files here
```

### 4. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Copy `.env.example` to `.env` and fill in your details:

```bash
cp .env.example .env
```

Edit `.env`:
```
GITHUB_TOKEN=ghp_YOUR_TOKEN_HERE
GITHUB_USERNAME=your_username
GITHUB_REPO=demo-repo
```

Replace:
- `ghp_YOUR_TOKEN_HERE` with your actual token (starts with `ghp_`)
- `your_username` with your GitHub username
- `demo-repo` with your test repository name

### 7. Run the Demo

```bash
python demo.py
```

---

## Expected Output

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║      GitHub API CRUD Demo - Full Tutorial               ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝


============================================================
  STEP 1: Verify Authentication
============================================================
  ✓ Authenticated as: your_username
  Name: Your Name
  Public repos: 42

============================================================
  STEP 2: Get Repository Information
============================================================
  ✓ Repository: your_username/demo-repo
  Description: Test repository for API demo
  Stars: 0
  Language: None
  Visibility: Public

============================================================
  STEP 3: CREATE - Create a New Issue
============================================================
  Issue title: Update documentation with API examples
  Labels: ['documentation', 'enhancement']
  ✓ Issue created with number: #1

  Issue #1: Update documentation with API examples
  State: open
  Created: 2024-04-13T10:30:00Z
  Updated: 2024-04-13T10:30:00Z
  Body: The README needs more practical examples for API integration...

============================================================
  STEP 4: READ - Retrieve Specific Issue
============================================================
  Fetching issue #1...
  ✓ Issue retrieved successfully

  Issue #1: Update documentation with API examples
  ...

============================================================
  STEP 5: UPDATE - Modify the Issue
============================================================
  Updating issue #1...
  New title: Update documentation with API examples (UPDATED)
  ✓ Issue updated successfully
  ...

============================================================
  STEP 6: READ - List All Issues
============================================================
  Fetching all issues...
  ✓ Retrieved 1 issue(s)
    • #1: Update documentation with API examples (UPDATED) (open)

============================================================
  STEP 7: DELETE - Close the Issue
============================================================
  Closing issue #1...
  ✓ Issue #1 closed successfully
  State: closed

============================================================
  STEP 8: Pull Request Operations
============================================================
  Note: Creating a PR requires an existing branch.
  For demonstration, we'll just list existing PRs.

  ✓ Retrieved 0 PR(s)
  (No pull requests found)

============================================================
  DEMO SUMMARY
============================================================

  Operations Performed:
    ✓ Authentication: Verified
    ✓ Repository Info: Retrieved
    ✓ Create Issue: Success
    ✓ Read Issue: Success
    ✓ Update Issue: Success
    ✓ List Issues: Success
    ✓ Delete Issue: Success

  Repository Statistics:
    Total issues: 1

  Next Steps:
    1. Modify the sample data in config.py
    2. Add more operations (comments, reactions, etc.)
    3. Integrate with a database to store results
    4. Build a web dashboard with the API data

✓ Demo completed successfully!
```

---

## Understanding the Code

### 1. Config File (`config.py`)
- Stores environment variables
- Defines API endpoints
- Contains sample data
- Sets up logging

### 2. API Client (`github_api_client.py`)
- Main class for all API operations
- Handles authentication
- Makes HTTP requests
- Error handling and logging
- CRUD methods for issues and PRs

### 3. Demo Script (`demo.py`)
- Demonstrates each CRUD operation
- Shows real-world usage
- Provides formatted output
- Includes error handling

---

## API Operations Explained

### CREATE - Create a New Issue
```python
success, response = client.create_issue(
    title="Update documentation",
    body="The README needs more examples",
    labels=["documentation"]
)
```

**API Call:**
```
POST /repos/{owner}/{repo}/issues
{
  "title": "Update documentation",
  "body": "The README needs more examples",
  "labels": ["documentation"]
}
```

### READ - Get a Specific Issue
```python
success, response = client.get_issue(issue_number=1)
```

**API Call:**
```
GET /repos/{owner}/{repo}/issues/1
```

### READ - List All Issues
```python
success, issues = client.list_issues(state="all")
```

**API Call:**
```
GET /repos/{owner}/{repo}/issues?state=all&per_page=100
```

### UPDATE - Modify an Issue
```python
success, response = client.update_issue(
    issue_number=1,
    title="New title",
    state="open"
)
```

**API Call:**
```
PATCH /repos/{owner}/{repo}/issues/1
{
  "title": "New title",
  "state": "open"
}
```

### DELETE - Close an Issue
```python
success, response = client.update_issue(issue_number=1, state="closed")
```

**API Call:**
```
PATCH /repos/{owner}/{repo}/issues/1
{
  "state": "closed"
}
```

---

## Troubleshooting

### Error: "401 Unauthorized"
**Cause:** Invalid or expired token
**Solution:**
1. Check if token is correctly copied to `.env`
2. Verify token hasn't expired
3. Regenerate token at https://github.com/settings/tokens

### Error: "404 Not Found"
**Cause:** Repository doesn't exist or name is wrong
**Solution:**
1. Verify repo name in `.env` matches GitHub
2. Check if repository is accessible
3. Ensure you're using the correct username

### Error: "422 Unprocessable Entity"
**Cause:** Invalid data or validation error
**Solution:**
1. Check required fields are provided
2. Validate data format
3. Review error message in response

### Error: "403 Forbidden"
**Cause:** Rate limit exceeded or insufficient permissions
**Solution:**
1. Wait 1 hour before retrying
2. Check token scopes include "repo"
3. Verify account has access to repository

### Error: "Connection refused"
**Cause:** Network issue
**Solution:**
1. Check internet connection
2. GitHub API might be down
3. Check firewall/proxy settings

---

## Rate Limiting

GitHub API has rate limits:
- **Unauthenticated:** 60 requests/hour
- **Authenticated:** 5000 requests/hour

Check your rate limit:
```bash
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/rate_limit
```

---

## Extending the Demo

### Add Comments to Issues
```python
def add_comment(self, issue_number: int, body: str):
    endpoint = f"/repos/{self.username}/{self.repo}/issues/{issue_number}/comments"
    return self._make_request("POST", endpoint, {"body": body})
```

### Add Reactions to Issues
```python
def add_reaction(self, issue_number: int, reaction: str):
    # reaction: "+1", "-1", "laugh", "confused", "heart", "rocket", "eyes"
    endpoint = f"/repos/{self.username}/{self.repo}/issues/{issue_number}/reactions"
    return self._make_request("POST", endpoint, {"content": reaction})
```

### Get Issue Comments
```python
def get_comments(self, issue_number: int):
    endpoint = f"/repos/{self.username}/{self.repo}/issues/{issue_number}/comments"
    return self._make_request("GET", endpoint)
```

---

## Best Practices

1. **Never hardcode secrets** - Always use environment variables
2. **Validate input** - Check data before sending to API
3. **Handle errors gracefully** - Use try-except blocks
4. **Implement rate limiting** - Add delays between requests
5. **Log operations** - Track what's happening
6. **Use test repositories** - Don't test on production
7. **Check response codes** - Different codes mean different things
8. **Document your code** - Make it easy for others

---

## Resources

- **GitHub API Docs:** https://docs.github.com/en/rest
- **Personal Access Tokens:** https://github.com/settings/tokens
- **Rate Limiting:** https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api
- **Requests Library:** https://requests.readthedocs.io/
- **Python Dotenv:** https://python-dotenv.readthedocs.io/

---

## Next Steps

1. ✓ Understand CRUD operations
2. ✓ Get comfortable with APIs
3. → Add database integration
4. → Build a web dashboard
5. → Deploy to production
6. → Add more GitHub operations (labels, milestones, etc.)

---

## License

MIT - Feel free to use this for learning and projects!

---

## Questions?

- Check the detailed guide: `GITHUB_API_DEMO_GUIDE.md`
- Review the code comments
- Check GitHub API documentation
- Add `print()` statements to debug

Happy coding! 🚀
