# AuthHub

**AuthHub** is a lightweight GitHub-based authentication system designed to simulate GitHub-style login functionality using secure credential handling, REST API interactions, and personal access tokens. It supports login, password reset, and username update features — all built using Python and GitHub's API.

---

## 🔐 Features

- GitHub-hosted credential database (private repo)
- Passwords securely hashed using PBKDF2 (SHA-256)
- Fully functional login, username reset, and password reset system
- API token-based authentication to manage and update user data via GitHub
- No storage or tracking of plaintext passwords

---

## ⚙️ Requirements

Before running AuthHub, complete the following setup steps:

1. **Create a GitHub Repository**
   - Create a new repository on your GitHub account
   - Set it to **private** to protect sensitive credential hashes

2. **Generate a GitHub Personal Access Token**
   - Navigate to: `GitHub > Settings > Developer Settings > Personal Access Tokens (Classic)`
   - Click **"Generate new token (classic)"**
   - Set expiration to your desired session duration (this can represent user timeout as well)
   - Select the following scopes:
     - `repo` (Full control of private repositories)
     - `delete_repo` (if you intend to remove or reset data)
   - Copy and store the token securely (you’ll use it in the script)

3. **Create a Users Folder in Your Repository**
   - Inside your GitHub repo, create a folder named `Users/`
   - For each user:
     - Create a subfolder named after their username
     - Inside that subfolder:
       - Create a file named `<username>.arz` — this will contain the hashed username
       - Create a file named `pass_<username>.arz` — this will contain the hashed password
   - All files should contain only the hash — AuthHub does **not** track real passwords

---

## 🛠️ Configuration

1. Open the project file in any text/code editor
2. Replace the following placeholders with your real values:
   - `"YOUR-GITHUB-USER"` — your GitHub username
   - `"YOUR-GITHUB-REPO"` — the name of your private GitHub repo
   - `"YOUR-OWN-KEY"` — your GitHub Personal Access Token

---

## 🚀 Running the Application

To start using AuthHub:

```bash
python authhub.py
```
Understand that this is a whole **function** meaning that you should use this to run with your main program as well as this is just a backend for a software.
