import os
import json
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Load tokens
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

app = App(token=SLACK_BOT_TOKEN)

def ensure_label(repo, label):
    url = f"https://api.github.com/repos/{repo}/labels"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        existing = [l["name"] for l in r.json()]
        if label not in existing:
            create = requests.post(url, headers=headers, json={"name": label})
            return create.status_code in [200, 201]
    return False

def create_issue(issue_data):
    repo = issue_data["repo"]
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    labels = issue_data.get("labels", [])
    for label in labels:
        ensure_label(repo, label)

    payload = {
        "title": issue_data["title"],
        "body": issue_data["body"],
        "labels": labels
    }

    print("\n📤 Payload sent to GitHub:")
    print(json.dumps(payload, indent=2))
    print(f"📍 Endpoint: {url}")

    r = requests.post(url, headers=headers, json=payload)

    print("📬 GitHub responded:")
    print(f"Status: {r.status_code}")
    print(r.text)

    try:
        return r.status_code, r.json()
    except json.JSONDecodeError:
        return r.status_code, {"message": r.text}

@app.command("/create-issues")
def handle_create_issues(ack, respond, command):
    ack()
    try:
        data = json.loads(command["text"])
        messages = []
        for item in data:
            status_code, result = create_issue(item)
            if status_code == 201:
                messages.append(f"✅ Created: <{result['html_url']}|{result['title']}>")
            else:
                messages.append(f"❌ Failed: {item['title']} ({result.get('message', 'Unknown error')})")
        respond("\n".join(messages))
    except Exception as e:
        respond(f"❌ Error processing request: {str(e)}")

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
