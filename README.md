<p align="center">
  <img src="assets/huemanatee-logo.svg" alt="Huemanatee" width="400">
</p>

<p align="center">
  <strong>Make AI prose sound human.</strong><br>
  Cut the plastic sheen. Keep the meaning.<br>
  Leave the facts to the author.
</p>

<p align="center">
  <a href="#install"><img
    src="https://img.shields.io/badge/runs%20in-Claude%20Code%20%C2%B7%20Codex%20%C2%B7%20Gemini%20%C2%B7%20Cursor%20%C2%B7%2075%2B%20agents-7FA7E6?style=flat-square"
    alt="Runs in Claude Code, Codex, Gemini, Cursor and 75+ agents"></a>
  <img
    src="https://img.shields.io/badge/format-plain%20SKILL.md-444C56?style=flat-square"
    alt="Distributed as plain SKILL.md files">
  <a href="#automatic-activation"><img
    src="https://img.shields.io/badge/Claude%20%26%20Codex-automatic%20prompt%20hook-A96A38?style=flat-square"
    alt="Automatic prompt hooks for Claude Code and Codex"></a>
</p>

<p align="center">
  A writing skill for turning stiff, over-balanced drafts into clear prose
  without padding the copy or making up specifics.
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#update">Update</a> ·
  <a href="#automatic-activation">Automatic activation</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#scope">Scope</a>
</p>

---

## Install

### Claude Code

```text
/plugin marketplace add GentBajko/huemanatee
/plugin install huemanatee@huemanatee-marketplace
```

This installs the skill and its prompt hook.

### Hosts that use the Skills CLI

The Skills CLI installs the skill bundle, including its `references/`
file:

```bash
npx skills add GentBajko/huemanatee
```

To target a host or install globally:

```bash
npx skills add GentBajko/huemanatee --agent codex --global
npx skills add GentBajko/huemanatee --agent cursor --global
```

The skill files travel with the install. Host-level hooks are configured
separately; see [Automatic activation](#automatic-activation).

## Update

| Installed with | Update with |
| --- | --- |
| Claude Code plugin | `claude plugin marketplace update huemanatee-marketplace`<br>then `claude plugin update huemanatee@huemanatee-marketplace` |
| `npx skills` | `npx skills update` |

Restart the host after a plugin update if it keeps an older copy of the
skill or hook.

## Automatic activation

The Claude Code marketplace plugin and the Codex plugin include a
`UserPromptSubmit` hook. It looks for requests to rewrite or humanize
prose, including drafts described as robotic or ChatGPT-like. When a
prompt fits, the hook reminds the host to use Huemanatee and its tell
catalog.

The hook ignores source code, configuration, and machine-readable output.
If the user names Huemanatee directly, the skill still applies when the
target is prose.

Codex may ask for permission to trust the bundled hook before running it.
That is a one-time safety check for plugin-provided commands.

Hooks belong to the host. `npx skills` installs skill files; it does not
edit each host's global hook configuration. The native prompt hooks are:

| Host | Prompt hook | Huemanatee status |
| --- | --- | --- |
| Claude Code | `UserPromptSubmit` | Bundled in the marketplace plugin |
| Codex | `UserPromptSubmit` | Bundled in `.codex-plugin` |
| Gemini CLI | `BeforeAgent` | Supported by Gemini, but not installed by `npx skills` |
| Cursor | `beforeSubmitPrompt` | Supported by Cursor; use skill discovery for context injection |

See the host documentation for [Claude hooks](https://code.claude.com/docs/en/hooks),
[Codex hooks](https://developers.openai.com/codex/hooks),
[Gemini CLI hooks](https://github.com/google-gemini/gemini-cli/blob/main/docs/hooks/reference.md),
and [Cursor hooks](https://cursor.com/docs/hooks).

## How it works

Huemanatee keeps the rewrite contract simple:

- Keep the meaning and the writer's dialect. Cut throat-clearing; a
  shorter result is fine.
- Do not make up metrics, anecdotes, or other facts. If the draft needs
  something only its author can supply, leave a marked slot.
- Return the rewrite by itself unless the user asks for commentary.
- Spend words where the argument needs them. Skip the obvious parts.

Before a longer rewrite, the skill reads
[`references/tells.md`](skills/huemanatee/references/tells.md). It covers
stock phrases, uniform rhythm, fake parallelism, unnecessary headings,
summary closers, and brochure-like tone.

## Scope

Use Huemanatee for blog posts, articles, marketing copy, release notes,
READMEs, and other prose. It is not for source code, configuration files,
structured data, or machine-readable output.

If the goal is to pass an AI detector, Huemanatee can make the writing
less synthetic to human readers, but it cannot promise a classifier result.
High-stakes authorship still needs details and edits from the actual author.
