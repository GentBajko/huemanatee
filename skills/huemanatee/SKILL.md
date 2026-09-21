---
name: huemanatee
description: Rewrite or edit text to remove AI-writing tells and read
  like a competent human wrote it. Not for source code, configs, or
  machine-read output. Use when the user asks to rewrite, edit,
  humanize, or de-AI text, says something sounds robotic or like
  ChatGPT, or requests polished prose for publication (blog posts,
  articles, marketing copy, release notes, READMEs).
---

# Humanish writing

The baseline rules live in CLAUDE.md and always apply. This skill adds
the full workflow for dedicated rewrites and longer pieces.

Read `references/tells.md` before drafting anything over a few
sentences. Density is the standard: two catalog items in one paragraph
means rewrite the paragraph.

## Rewrite contract

When the task is "humanize/rewrite this text":
- Preserve meaning, coverage, format, and the original's dialect.
- Length may shrink — cutting throat-clearing is the job. Never pad.
- Output only the rewrite. No preamble, no change log, unless asked.
- If the text needs a specific only the author has (a metric, an
  anecdote), ask or leave a marked slot like `[your number]`.
  Invented specificity is worse than blandness.

## Beyond the ban lists

- Spend words proportional to importance. Symmetric coverage of every
  subtopic is a tell; skip the obvious, go deep where it matters.
- One verifiable specific outweighs three generic benefits. If a
  sentence could appear unchanged in any article on the topic, cut it
  or sharpen it.
- Commit when a position is asked for. Hedge only when uncertainty is
  real, and say what would resolve it.
- Register comes from the venue, not from any example: a Slack reply
  is not a report.

## Example (technique, not target voice)

Before:
> In today's fast-paced digital landscape, effective onboarding isn't
> just a nice-to-have — it's a game-changer. It streamlines workflows,
> boosts engagement, and drives retention. Ultimately, investing in
> onboarding is a testament to a company's commitment to its people.

After (numbers are author-supplied — never invent them):
> Good onboarding pays for itself. When we cut the setup checklist
> from [34] steps to [9], new hires shipped their first PR in [four]
> days instead of [eleven]. Most companies never measure this. That's
> why most onboarding stays bad.

## Final pass — mandatory for anything over ~150 words

1. Grep: "not just", "not only", em dash count > 1, summary closers,
   every ban-list word in `references/tells.md`.
2. Shape: bold-colon bullets? Triads? Sentence lengths clustered
   around 15 words? Same-shaped consecutive openers (unless deliberate)?
3. Ending: if the last paragraph summarizes, delete it and fold any
   new idea upward.
4. Substance: does each major point carry one checkable specific?

Fix by restructuring, not word-swapping.

If the user's goal is passing AI detectors: state plainly that these
rules reduce recognizability to humans but don't guarantee passing
classifiers, and that high-stakes authorship needs hand edits with
details only they know.
