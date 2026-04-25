# GitHub API Demo - Complete Step-by-Step Guide

## Project Overview
This demo shows how to interact with GitHub's REST API using Python to perform CRUD operations on:
- Issues (Create, Read, Update, Delete)
- Repositories (Read, List)
- Pull Requests (Create, List, Update)

---

## Step 1: Prerequisites & Setup

### 1.1 Install Required Libraries
```bash
pip install requests python-dotenv
```

### 1.2 Get Your GitHub Personal Access Token
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Select scopes:
   - `repo` (full control of private repositories)
   - `admin:repo_hook` (write access to hooks)
   - `user` (read user profile data)
4. Copy the token (you won't see it again!)

### 1.3 Environment Setup
Create a `.env` file in your project directory:
```
GITHUB_TOKEN=your_token_here
GITHUB_USERNAME=your_username
GITHUB_REPO=demo-repo
```

---

## Step 2: Project Structure
```
github-api-demo/
├── .env                          # Your credentials (never commit!)
├── .gitignore                    # Add .env to this
├── config.py                     # Configuration and constants
├── github_api_client.py          # Main API wrapper class
├── demo.py                       # Main demonstration script
├── requirements.txt              # Dependencies
└── README.md                     # Documentation
```

---

## Step 3: Understanding GitHub API Basics

### Base URL
- REST API v3: `https://api.github.com`

### Authentication
- Header: `Authorization: token YOUR_TOKEN`
- Rate limit: 60 requests/hour (unauthenticated), 5000/hour (authenticated)

### Common Endpoints for Demo
```
GET    /repos/{owner}/{repo}
GET    /repos/{owner}/{repo}/issues
POST   /repos/{owner}/{repo}/issues
PATCH  /repos/{owner}/{repo}/issues/{issue_number}
DELETE /repos/{owner}/{repo}/issues/{issue_number}
GET    /repos/{owner}/{repo}/pulls
POST   /repos/{owner}/{repo}/pulls
PATCH  /repos/{owner}/{repo}/pulls/{pull_number}
```

---

## Step 4: API Response Examples

### Create Issue Response
```json
{
  "id": 1296269,
  "number": 1347,
  "title": "Found a bug",
  "body": "I'm having a problem with this.",
  "state": "open",
  "created_at": "2011-04-22T13:33:48Z",
  "updated_at": "2011-04-22T13:33:48Z"
}
```

### List Issues Response
```json
[
  {
    "number": 1347,
    "title": "Found a bug",
    "state": "open",
    "created_at": "2011-04-22T13:33:48Z"
  }
]
```

---

## Step 5: Data Preparation

### Sample Data for Demo
```python
# Issue data
issue_data = {
    "title": "Update documentation",
    "body": "The README needs more examples",
    "labels": ["documentation", "enhancement"],
    "assignees": ["username"]
}

# Pull Request data
pr_data = {
    "title": "Add new feature",
    "body": "This PR adds XYZ functionality",
    "head": "feature-branch",
    "base": "main"
}
```

---

## Step 6: Running the Demo

### 6.1 Create a Test Repository
Before running the demo, create a test repository on GitHub:
1. Go to https://github.com/new
2. Name it `demo-repo` (or as per your .env file)
3. Keep it public or private (both work)
4. Don't initialize with files

### 6.2 Run the Demo
```bash
python demo.py
```

### 6.3 What You'll See
```
=== GitHub API CRUD Demo ===
1. Creating an issue...
   ✓ Issue created: #1 - "Update documentation"

2. Reading the issue...
   ✓ Issue retrieved successfully
   State: open, Created: 2024-04-13T10:30:00Z

3. Updating the issue...
   ✓ Issue updated successfully
   New state: closed

4. Listing all issues...
   ✓ Found 1 issue(s)

5. Creating a pull request...
   ✓ PR created: #2 - "Add new feature"

6. Listing pull requests...
   ✓ Found 1 PR(s)

7. Cleaning up...
   ✓ Issue deleted successfully

=== Demo Complete! ===
```

---

## Step 7: API Rate Limiting & Error Handling

### Check Rate Limit
```bash
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/rate_limit
```

### Common Status Codes
- `200`: Success
- `201`: Created
- `204`: Deleted
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden (rate limited)
- `404`: Not Found
- `422`: Validation Failed

---

## Step 8: Best Practices

1. **Never hardcode tokens** - Always use .env files
2. **Handle rate limits** - Implement exponential backoff
3. **Validate inputs** - Check data before sending to API
4. **Use try-except blocks** - Handle network errors gracefully
5. **Log operations** - Track what's happening
6. **Test with a test repo** - Don't use production repos
7. **Document your endpoints** - Keep track of what you're using

---

## Step 9: Extending the Demo

### Add More Operations
- Get repository details
- Manage labels
- Manage milestones
- Add comments to issues
- React to issues/PRs
- Manage collaborators

### Add Database Integration
- Store API responses in SQLite/PostgreSQL
- Track changes over time
- Build a dashboard

### Add Scheduling
- Use APScheduler to run checks periodically
- Auto-close stale issues
- Generate reports

---

## Step 10: Troubleshooting

### Issue: "401 Unauthorized"
- Check if token is correct in .env
- Token may have expired - regenerate it

### Issue: "404 Not Found"
- Verify repository name is correct
- Check repository is accessible by your account

### Issue: "422 Unprocessable Entity"
- Validate input data
- Check required fields are present
- Branch names must exist for PR creation

### Issue: "Rate limit exceeded"
- Wait an hour before retrying
- Use GraphQL API for more efficient queries

---

## Additional Resources

- GitHub API Docs: https://docs.github.com/en/rest
- REST API Reference: https://docs.github.com/en/rest/reference
- Authentication: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

