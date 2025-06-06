✅ LLM Instruction Block: “Generate GitHub-Ready JSON Issues for FlatBoxBot”
You are generating structured JSON that describes GitHub issues for a Slack-integrated automation bot called FlatBoxBot.

Each entry must include the following fields:

"repo": full repo name (e.g., "your-username/repo-name")

"title": formatted with a type prefix such as Epic:, User Story:, or Subtask:

"body": a Markdown-formatted string containing type-specific sections

"labels": array of short labels such as "epic", "Q2", "SP: 5"

"project_field_values": must include "Status" with one of: "To Do", "In Progress", "Review", "Blocked", or "Done"

"due_date": formatted as YYYY-MM-DD



Use this structure for the body field based on issue type:

EPIC
md
Copy
Edit
## Experience Phase
[Phase of user experience, e.g. Signup Flow]

## User Emotions
[How the user feels during this phase]

## Pain Points
- [Bullet list of user problems]

## Opportunity for Improvement
[Summary of what this Epic aims to fix]
USER STORY (Issue)
md
Copy
Edit
## User Story
As a [role], I want [feature] so that [benefit].

## Story Points
[Fibonacci estimate: 1, 2, 3, 5, 8, 13]

## Environment
[Where it applies: Mobile, Web, API, etc.]

## Related Epic
[Exact Epic title this story supports]
SUBTASK
md
Copy
Edit
## Instructions
[Step-by-step guide for implementing this task]

## Acceptance Criteria
- [ ] [Checkbox items that must be satisfied]

## Necessary Documentation
- [ ] [Links or output files to be updated]



Let me know if you want it formatted for Claude prompt wrapping, too.


✅ LLM Instruction Block: Generate GitHub-Ready JSON for FlatBoxBot
You are generating structured JSON that describes GitHub issues for automated creation via Slack and FlatBoxBot. Output must be a valid JSON array of issue objects. Each object should match one of the following types: Epic, User Story, or Subtask. Follow the formatting rules and structure exactly.

Global Rules
Output must be a JSON array, no Markdown or extra text.

All issues must include:

repo (format: username/repo-name)

title

body (formatted in GitHub markdown)

labels (array of strings)

project_field_values with a "Status" key

due_date in YYYY-MM-DD format

Status must be one of: "To Do", "In Progress", "Review", "Blocked", "Done"

Types
1. Epic
Title Prefix: Epic:

Labels: must include "epic" plus any relevant tags

Body Format:

shell
Copy
Edit
## Experience Phase
[Name of journey stage]

## User Emotions
[What users feel in this phase]

## Pain Points
- [List of friction points]

## Opportunity for Improvement
[Description of how we can improve the experience]
2. User Story (Issue)
Title Prefix: User Story:

Labels: must include "user-story" and a "SP: [number]" label for story points

Body Format:

css
Copy
Edit
## User Story
As a [user role], I want to [action], so that [goal or benefit].

## Story Points
[1, 2, 3, 5, 8, 13, etc.]

## Environment
[Web, mobile, API, etc.]

## Related Epic
[Exact title of related epic, e.g., "Epic: Auth Revamp"]
3. Subtask
Title Prefix: Subtask:

Labels: must include "subtask" plus any relevant tags

Body Format:

shell
Copy
Edit
## Instructions
[Clear, technical steps on what needs to be done]

## Acceptance Criteria
- [ ] [Bullet-style checklist of what must be true for completion]

## Necessary Documentation
- [ ] [What to update, create, or link to]


  ...
]
Let me know if you want me to generate a prompt-ready block in plaintext or JSON-friendly string format for direct copy/paste into your build pipeline.