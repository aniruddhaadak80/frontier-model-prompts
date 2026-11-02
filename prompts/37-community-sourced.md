# 🌐 Community-Sourced Prompts - real prompts from Reddit, X, and prompt platforms

> Curated from public community posts (Sept–Oct 2026). Attribution-first. Each prompt is quoted or adapted from a public post; links in SOURCES.md. These are starting points — adapt to your task.

## GPT-6 Astra

### 1. Initiative & follow-through (OpenAI-recommended)
```
You should infer the user's intent and task scope from the instructions and prior conversation context. Your job is to bias towards action and carry the user's intended task to completion.

When the user expresses intent to perform new work or fix an existing issue, persist until the user's intended goal is complete. Progress autonomously towards the user's goal (creating isolated worktrees/checkouts if needed, resolving merge conflicts, read-only actions, creating draft PRs) unless clearly destructive or irreversible.
```

### 2. Campaign brief (r/promptingmagic)
```
Develop a campaign for [offer] aimed at [buyer]. Use the attached customer interviews and product facts. First identify the strongest buying problem and the evidence supporting it. Create a campaign brief, a landing-page draft, three email drafts, five LinkedIn posts, and three visual directions. Keep the central promise consistent. Link customer insights to source passages. Do not invent testimonials, performance claims, or customer quotes. Finish with a simple measurement plan and the assumptions we should test first. Prepare everything for review; do not publish or send it.
```

### 3. Motion graphics brief (r/promptingmagic)
```
You are a motion designer. Produce a 20-30s landscape video for [audience] whose one takeaway is [message]. Map every scene to a visual action and a purpose; put the most compelling image near the start. Establish the look with reference images, colors, type, logos, and exact wording; provide representative still frames. Preview the hardest moment before committing. Refine timing, text, sound, transitions, and the exported file. Keep the source editable.
```

### 4. Continue-the-mission loop (r/ChatGPT)
```
Mission: [explicit mission declaration with goal, scope, and stop conditions].

Every subsequent turn, the user will only say "continue the mission". Treat that as permission to continue executing the same mission from its existing state. Do not re-ask the goal. Report progress each turn and stop only at a defined stop condition or when blocked.
```

### 5. RTS game (community, multi-day)
```
Build a StarCraft-inspired RTS with two factions, 3D units, and voice lines. Use 3D AI Studio for models and ElevenLabs for voices. Keep the scope to a weekend build first; list cut/keep. Include pause, restart, mute, tutorial. Plan a self-playtest pass.
```

## Claude Opus 5.5

### 6. Launch video, one prompt (r/SaaS)
```
You're a world-class motion designer building a [product] launch video. Research and land our core value and narrative. Scenes should be dynamic and confident: hook in the first second, then distinct beats for product proof. Brand-accurate UI, type, color, and motion. Score the music so every cut, animation hit, and scene change lands on a beat or drop; retimed until synced. Social energy, quick cuts.
```

### 7. Typing game, end to end (r/ClaudeAI)
```
Build a fun, extremely smooth typing game end to end. It should measure your speed but be genuinely fun to practice with, and adapt up and down to skill so progression feels fair. Free website, global leaderboard, optional GitHub or X username to show avatar (no sign-in). Fully responsive. Visually test everything, test the mechanics, and keep iterating until it's something you're proud to show off. Use Sonnet 5.5 subagents for well-defined parallel tasks, track usage and timing separately, and open it in my browser when done.
```

### 8. Effort-for-planning note (r/claude)
```
Plan on medium effort for speed; escalate to high only for genuinely hard subproblems. Scope the plan tightly and give enough context. Do not over-engineer; measure whether the extra effort changed the outcome before committing.
```

## Prompting patterns

### 9. Time-budgeted agent teams (Opus 5.5 guide)
```
Track elapsed time against a budget (e.g., "elapsed 340s / 1200s") so a team of agents paces itself and finishes sooner. Report progress between tool calls; do not treat a progress update as "done".
```

### 10. Delegation clarity (r/OpenaiCodex)
```
Aggressively delegate any task that is bounded and straightforward to [subagent]. Define "bounded and straightforward" precisely (e.g., single-file, reversible, no external side effects) so the model actively seeks delegation opportunities instead of interpreting "when adequate" loosely.
```

### 11. Stop-before-destructive gates (universal)
```
Authorized scope: [folders/apps/sites]. Stop before any destructive, irreversible, sending, purchasing, deleting, or permission-changing step; require explicit approval. Work read-only and reversible actions autonomously. Redact PII. Log evidence.
```

### 12. Verification proportional to risk (universal)
```
Verification: keep checks proportional to risk. Small reversible changes -> targeted checks. Risky changes -> full relevant suite. End with a Done checklist (complete/partial/blocked) with evidence links, plus assumptions and what was not verified.
```

### 13. Concise paragraphs, no slop (Astra style)
```
Default to concise paragraphs. Lists only for parallel/sequential items. Plain verbs, active voice. One idea per paragraph, main point early. No slop words or contrastive phrasing. State what to do; avoid saying what you won't do.
```

### 14. Honest sourcing (research)
```
Cite every non-obvious claim with a link; mark confidence high/medium/low. Prefer primary sources; label secondary inference explicitly. Flag contradictions instead of smoothing them over. Do not fabricate URLs.
```

### 15. Structured output with unknown (universal)
```
Use schema enforcement for shape; prompt for judgment. Enums closed; include "unknown" with a reason field. Require evidence spans for extracted facts. Validate totals, dates, units. Version the schema.
```

---

*Attribution: prompts adapted from public Reddit posts (r/coding_agents, r/promptingmagic, r/OpenaiCodex, r/ChatGPT, r/ClaudeAI, r/SaaS, r/claude) and OpenAI/Anthropic prompting guides, Sept–Oct 2026. See SOURCES.md.*