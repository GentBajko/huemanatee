#!/usr/bin/env python3
"""Suggest the Huemanatee skill when a submitted prompt asks for prose humanization."""

import json
import re
import sys


TRIGGER = re.compile(
    r"(?:"
    r"\bhuemanatee\b"
    r"|"
    r"\b(?:rewrite|rephrase|paraphrase|edit|polish|revise)\b.*"
    r"\b(?:human|natural|robotic|ai|chatgpt|prose|writing|sound|read)\b"
    r"|\b(?:make|sound|read|feel)\b.{0,80}\b(?:human|natural|less robotic|less like ai|less like chatgpt)\b"
    r"|\b(?:less|more)\s+(?:robotic|human|natural)\b"
    r"|\b(?:humani[sz](?:e|ation|ing)?|de[- ]?ai|de[- ]?robot|human-sounding)\b"
    r"|\b(?:robotic|chatgpt|ai[- ]?(?:written|generated|sounding))\b"
    r")",
    re.IGNORECASE | re.DOTALL,
)

CONTEXT = (
    "The submitted request appears to fit the huemanatee skill. For prose-only "
    "rewriting or humanization, use the installed huemanatee skill and read its "
    "references/tells.md when the draft is more than a few sentences. Preserve "
    "meaning and dialect, cut throat-clearing, and do not invent facts. Do not use "
    "it for source code, configuration, or machine-readable output; if the user "
    "explicitly names huemanatee, honor that request when the target is prose."
)


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, TypeError):
        return

    prompt = payload.get("user_prompt", payload.get("prompt", ""))
    if not isinstance(prompt, str) or not TRIGGER.search(prompt):
        return

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": CONTEXT,
                }
            }
        )
    )


if __name__ == "__main__":
    main()
