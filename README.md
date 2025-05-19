# GH_Flatbox

**GH_Flatbox** is a Slack-to-GitHub connector designed for teams and LLM workflows. It lets you generate structured GitHub issues and project board entries directly from Slack, using JSON templates—no context switching, no manual copy-paste.

Ideal for:
- Teams using LLMs or prompt workflows to autogenerate GitHub tasks, epics, and subtasks
- Automating project board population from Slack conversations

---

## Features

- **Slack Integration:** Use Slack commands or messages to trigger issue creation
- **Structured JSON Input:** Accepts well-formed JSON describing issues, epics, and subtasks
- **GitHub Automation:** Instantly creates issues in your chosen repo and updates project boards
- **Customizable Templates:** Supports Epics, User Stories, and Subtasks with rich metadata

---

## Example JSON Format

Send a JSON array to FlatBoxBot in Slack, following this structure:

```json
[
  {
    "repo": "your-username/repo-name",
    "title": "Epic: Onboarding Flow",
    "body": "## Experience Phase\nSignup\n\n## User Emotions\nCurious, hopeful\n\n## Pain Points\n- Confusing UI\n- Slow email verification\n\n## Opportunity for Improvement\nStreamline signup and clarify steps.",
    "labels": ["epic", "Q2"],
    "project_field_values": { "Status": "To Do" },
    "due_date": "2024-07-01"
  },
  {
    "repo": "your-username/repo-name",
    "title": "User Story: Fast Email Verification",
    "body": "## User Story\nAs a new user, I want instant email verification so that I can start using the app right away.\n\n## Story Points\n3\n\n## Environment\nWeb\n\n## Related Epic\nEpic: Onboarding Flow",
    "labels": ["user-story", "SP: 3"],
    "project_field_values": { "Status": "To Do" },
    "due_date": "2024-07-02"
  }
]
```

**Types supported:**  
- **Epic:** High-level project goals  
- **User Story:** Feature requests or requirements  
- **Subtask:** Technical or implementation steps

See [`HOW-To_project-board_GH_Flatbox.md`](HOW-To_project-board_GH_Flatbox.md) for full field and formatting details.

---

## How It Works

1. **Compose JSON**: Use the provided templates to describe your issues.
2. **Send to Slack**: Post the JSON to FlatBoxBot in your Slack workspace.
3. **Automated Creation**: The bot parses the JSON and creates issues in the specified GitHub repo, updating project boards as needed.

---

## Setup & Configuration

1. **Clone the repo** and install dependencies (language/framework-specific; e.g., `npm install` or `pip install -r requirements.txt`).
2. **Configure environment variables** (do not use `.env` files; inject via your shell or secrets manager):
    - `SLACK_BOT_TOKEN`
    - `SLACK_APP_TOKEN`
    - `GITHUB_TOKEN`
3. **Run the app** (example: `python main.py` or `node app.js`).
4. **Add FlatBoxBot to your Slack workspace** using the manifest in [`slack-_manifest_GH_Flatbox.json`](slack-_manifest_GH_Flatbox.json).

**Note:** All credentials must be provided securely via environment variables—never hardcoded or in plaintext files.

## Example Environment Variables

Set the following environment variables in your shell or secrets manager before running the app:

```sh
# Example: set these in your shell or CI/CD environment
export SLACK_BOT_TOKEN=your-slack-bot-token
export SLACK_APP_TOKEN=your-slack-app-level-token
export GITHUB_TOKEN=your-github-personal-access-token
```

**Important:**  
- **Never** commit secrets or `.env` files to your repository.  
- Inject these variables securely at runtime (via your shell, Docker, or a secrets manager).

---

## Slack App Permissions

- `commands`, `chat:write`, `channels:history`, `app_mentions:read`, `files:read`, etc.
- See [`slack-_manifest_GH_Flatbox.json`](slack-_manifest_GH_Flatbox.json) for the full list.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests.  
Make sure to follow security best practices and never commit secrets.

---

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

## Acknowledgments

- This project was developed with the assistance of ChatGPT-4o. The name "FlatBox" was suggested by ChatGPT-4o after a voice-to-text mishearing during development.

## Image Credits

Image: "Reusable shipping box by rhinopaq" by rhinopaq is licensed under CC BY-SA 4.0 (Creative Commons Attribution-Share Alike 4.0 International)  
Source: https://commons.wikimedia.org/wiki/File:Reusable_shipping_box_by_rhinopaq.jpg

