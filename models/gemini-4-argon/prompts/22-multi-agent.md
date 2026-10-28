# 🤖 Multi-Agent & Subagent Orchestration - 120 copyable Gemini 4 Argon prompts

> Explicit delegation: when, how much, and how agents report back.

> Target model: Gemini 4 Argon (`gemini-4-argon`). Sparse MoE with native multimodal (text/image/audio/video). Context 1M. Knowledge cutoff Mar 2026. Strong on knowledge work, finance/legal, cybersecurity defense.

> Safety: defensive / authorized-scope use only. Stop before destructive, irreversible, sending, purchasing, deleting, or permission-changing steps without approval.

**Jump:** [Model index](../../README.md) · [Search all](prompts_index.json)

How to use: click any prompt title to expand it top to bottom, then use the copy icon on the code block.

<details>
<summary><code>multi-agent-001</code> - split a research brief across three parallel subagents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Split a research brief across three parallel subagents in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>multi-agent-002</code> - coordinate a release crew: notes, QA, comms (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Coordinate a release crew: notes, QA, comms for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>multi-agent-003</code> - design an agent stop/ask/continue policy (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Design an agent stop/ask/continue policy for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>multi-agent-004</code> - orchestrate a data pipeline: extract, validate, load agents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Orchestrate a data pipeline: extract, validate, load agents for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>multi-agent-005</code> - run a docs-sync crew across repos (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Run a docs-sync crew across repos for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>multi-agent-006</code> - build a critic loop: drafter, checker, fixer (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a critic loop: drafter, checker, fixer with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>multi-agent-007</code> - build a meeting-to-actions pipeline with owners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Build a meeting-to-actions pipeline with owners in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>multi-agent-008</code> - run competing solution spikes then merge winners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Run competing solution spikes then merge winners for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>multi-agent-009</code> - coordinate a test-generation swarm per module (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Coordinate a test-generation swarm per module for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>multi-agent-010</code> - coordinate a migration crew with ownership zones (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Coordinate a migration crew with ownership zones for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>multi-agent-011</code> - orchestrate a translation-plus-glossary crew (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Orchestrate a translation-plus-glossary crew for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>multi-agent-012</code> - build a map-reduce doc review with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a map-reduce doc review with merge rules with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>multi-agent-013</code> - run a red-vs-blue review (defensive) with judges (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Run a red-vs-blue review (defensive) with judges in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>multi-agent-014</code> - orchestrate design+code+QA agents with handoffs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Orchestrate design+code+QA agents with handoffs for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>multi-agent-015</code> - build a support-triage swarm with escalation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a support-triage swarm with escalation for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>multi-agent-016</code> - split a research brief across three parallel subagents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Split a research brief across three parallel subagents for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>multi-agent-017</code> - coordinate a release crew: notes, QA, comms (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Coordinate a release crew: notes, QA, comms for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>multi-agent-018</code> - design an agent stop/ask/continue policy (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Design an agent stop/ask/continue policy with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>multi-agent-019</code> - orchestrate a data pipeline: extract, validate, load agents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Orchestrate a data pipeline: extract, validate, load agents in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>multi-agent-020</code> - run a docs-sync crew across repos (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Run a docs-sync crew across repos for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>multi-agent-021</code> - build a critic loop: drafter, checker, fixer (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a critic loop: drafter, checker, fixer for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>multi-agent-022</code> - build a meeting-to-actions pipeline with owners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Build a meeting-to-actions pipeline with owners for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>multi-agent-023</code> - run competing solution spikes then merge winners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Run competing solution spikes then merge winners for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>multi-agent-024</code> - coordinate a test-generation swarm per module (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Coordinate a test-generation swarm per module with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>multi-agent-025</code> - coordinate a migration crew with ownership zones (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Coordinate a migration crew with ownership zones in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>multi-agent-026</code> - orchestrate a translation-plus-glossary crew (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Orchestrate a translation-plus-glossary crew for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>multi-agent-027</code> - build a map-reduce doc review with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a map-reduce doc review with merge rules for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>multi-agent-028</code> - run a red-vs-blue review (defensive) with judges (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Run a red-vs-blue review (defensive) with judges for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>multi-agent-029</code> - orchestrate design+code+QA agents with handoffs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Orchestrate design+code+QA agents with handoffs for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>multi-agent-030</code> - build a support-triage swarm with escalation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a support-triage swarm with escalation with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>multi-agent-031</code> - split a research brief across three parallel subagents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Split a research brief across three parallel subagents in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 31.
```
</details>

<details>
<summary><code>multi-agent-032</code> - coordinate a release crew: notes, QA, comms (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Coordinate a release crew: notes, QA, comms for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 32.
```
</details>

<details>
<summary><code>multi-agent-033</code> - design an agent stop/ask/continue policy (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Design an agent stop/ask/continue policy for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 33.
```
</details>

<details>
<summary><code>multi-agent-034</code> - orchestrate a data pipeline: extract, validate, load agents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Orchestrate a data pipeline: extract, validate, load agents for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 34.
```
</details>

<details>
<summary><code>multi-agent-035</code> - run a docs-sync crew across repos (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Run a docs-sync crew across repos for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 35.
```
</details>

<details>
<summary><code>multi-agent-036</code> - build a critic loop: drafter, checker, fixer (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a critic loop: drafter, checker, fixer with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 36.
```
</details>

<details>
<summary><code>multi-agent-037</code> - build a meeting-to-actions pipeline with owners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Build a meeting-to-actions pipeline with owners in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 37.
```
</details>

<details>
<summary><code>multi-agent-038</code> - run competing solution spikes then merge winners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Run competing solution spikes then merge winners for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 38.
```
</details>

<details>
<summary><code>multi-agent-039</code> - coordinate a test-generation swarm per module (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Coordinate a test-generation swarm per module for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 39.
```
</details>

<details>
<summary><code>multi-agent-040</code> - coordinate a migration crew with ownership zones (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Coordinate a migration crew with ownership zones for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 40.
```
</details>

<details>
<summary><code>multi-agent-041</code> - orchestrate a translation-plus-glossary crew (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Orchestrate a translation-plus-glossary crew for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 41.
```
</details>

<details>
<summary><code>multi-agent-042</code> - build a map-reduce doc review with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a map-reduce doc review with merge rules with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 42.
```
</details>

<details>
<summary><code>multi-agent-043</code> - run a red-vs-blue review (defensive) with judges (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Run a red-vs-blue review (defensive) with judges in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 43.
```
</details>

<details>
<summary><code>multi-agent-044</code> - orchestrate design+code+QA agents with handoffs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Orchestrate design+code+QA agents with handoffs for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 44.
```
</details>

<details>
<summary><code>multi-agent-045</code> - build a support-triage swarm with escalation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a support-triage swarm with escalation for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 45.
```
</details>

<details>
<summary><code>multi-agent-046</code> - split a research brief across three parallel subagents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Split a research brief across three parallel subagents for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 46.
```
</details>

<details>
<summary><code>multi-agent-047</code> - coordinate a release crew: notes, QA, comms (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Coordinate a release crew: notes, QA, comms for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 47.
```
</details>

<details>
<summary><code>multi-agent-048</code> - design an agent stop/ask/continue policy (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Design an agent stop/ask/continue policy with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 48.
```
</details>

<details>
<summary><code>multi-agent-049</code> - orchestrate a data pipeline: extract, validate, load agents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Orchestrate a data pipeline: extract, validate, load agents in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 49.
```
</details>

<details>
<summary><code>multi-agent-050</code> - run a docs-sync crew across repos (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Run a docs-sync crew across repos for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 50.
```
</details>

<details>
<summary><code>multi-agent-051</code> - build a critic loop: drafter, checker, fixer (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a critic loop: drafter, checker, fixer for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 51.
```
</details>

<details>
<summary><code>multi-agent-052</code> - build a meeting-to-actions pipeline with owners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Build a meeting-to-actions pipeline with owners for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 52.
```
</details>

<details>
<summary><code>multi-agent-053</code> - run competing solution spikes then merge winners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Run competing solution spikes then merge winners for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 53.
```
</details>

<details>
<summary><code>multi-agent-054</code> - coordinate a test-generation swarm per module (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Coordinate a test-generation swarm per module with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 54.
```
</details>

<details>
<summary><code>multi-agent-055</code> - coordinate a migration crew with ownership zones (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Coordinate a migration crew with ownership zones in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 55.
```
</details>

<details>
<summary><code>multi-agent-056</code> - orchestrate a translation-plus-glossary crew (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Orchestrate a translation-plus-glossary crew for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 56.
```
</details>

<details>
<summary><code>multi-agent-057</code> - build a map-reduce doc review with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a map-reduce doc review with merge rules for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 57.
```
</details>

<details>
<summary><code>multi-agent-058</code> - run a red-vs-blue review (defensive) with judges (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Run a red-vs-blue review (defensive) with judges for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 58.
```
</details>

<details>
<summary><code>multi-agent-059</code> - orchestrate design+code+QA agents with handoffs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Orchestrate design+code+QA agents with handoffs for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 59.
```
</details>

<details>
<summary><code>multi-agent-060</code> - build a support-triage swarm with escalation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a support-triage swarm with escalation with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 60.
```
</details>

<details>
<summary><code>multi-agent-061</code> - split a research brief across three parallel subagents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Split a research brief across three parallel subagents in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 61.
```
</details>

<details>
<summary><code>multi-agent-062</code> - coordinate a release crew: notes, QA, comms (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Coordinate a release crew: notes, QA, comms for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 62.
```
</details>

<details>
<summary><code>multi-agent-063</code> - design an agent stop/ask/continue policy (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Design an agent stop/ask/continue policy for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 63.
```
</details>

<details>
<summary><code>multi-agent-064</code> - orchestrate a data pipeline: extract, validate, load agents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Orchestrate a data pipeline: extract, validate, load agents for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 64.
```
</details>

<details>
<summary><code>multi-agent-065</code> - run a docs-sync crew across repos (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Run a docs-sync crew across repos for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 65.
```
</details>

<details>
<summary><code>multi-agent-066</code> - build a critic loop: drafter, checker, fixer (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a critic loop: drafter, checker, fixer with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 66.
```
</details>

<details>
<summary><code>multi-agent-067</code> - build a meeting-to-actions pipeline with owners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Build a meeting-to-actions pipeline with owners in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 67.
```
</details>

<details>
<summary><code>multi-agent-068</code> - run competing solution spikes then merge winners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Run competing solution spikes then merge winners for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 68.
```
</details>

<details>
<summary><code>multi-agent-069</code> - coordinate a test-generation swarm per module (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Coordinate a test-generation swarm per module for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 69.
```
</details>

<details>
<summary><code>multi-agent-070</code> - coordinate a migration crew with ownership zones (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Coordinate a migration crew with ownership zones for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 70.
```
</details>

<details>
<summary><code>multi-agent-071</code> - orchestrate a translation-plus-glossary crew (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Orchestrate a translation-plus-glossary crew for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 71.
```
</details>

<details>
<summary><code>multi-agent-072</code> - build a map-reduce doc review with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a map-reduce doc review with merge rules with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 72.
```
</details>

<details>
<summary><code>multi-agent-073</code> - run a red-vs-blue review (defensive) with judges (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Run a red-vs-blue review (defensive) with judges in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 73.
```
</details>

<details>
<summary><code>multi-agent-074</code> - orchestrate design+code+QA agents with handoffs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Orchestrate design+code+QA agents with handoffs for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 74.
```
</details>

<details>
<summary><code>multi-agent-075</code> - build a support-triage swarm with escalation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a support-triage swarm with escalation for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 75.
```
</details>

<details>
<summary><code>multi-agent-076</code> - split a research brief across three parallel subagents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Split a research brief across three parallel subagents for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 76.
```
</details>

<details>
<summary><code>multi-agent-077</code> - coordinate a release crew: notes, QA, comms (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Coordinate a release crew: notes, QA, comms for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 77.
```
</details>

<details>
<summary><code>multi-agent-078</code> - design an agent stop/ask/continue policy (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Design an agent stop/ask/continue policy with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 78.
```
</details>

<details>
<summary><code>multi-agent-079</code> - orchestrate a data pipeline: extract, validate, load agents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Orchestrate a data pipeline: extract, validate, load agents in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 79.
```
</details>

<details>
<summary><code>multi-agent-080</code> - run a docs-sync crew across repos (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Run a docs-sync crew across repos for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 80.
```
</details>

<details>
<summary><code>multi-agent-081</code> - build a critic loop: drafter, checker, fixer (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a critic loop: drafter, checker, fixer for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 81.
```
</details>

<details>
<summary><code>multi-agent-082</code> - build a meeting-to-actions pipeline with owners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Build a meeting-to-actions pipeline with owners for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 82.
```
</details>

<details>
<summary><code>multi-agent-083</code> - run competing solution spikes then merge winners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Run competing solution spikes then merge winners for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 83.
```
</details>

<details>
<summary><code>multi-agent-084</code> - coordinate a test-generation swarm per module (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Coordinate a test-generation swarm per module with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 84.
```
</details>

<details>
<summary><code>multi-agent-085</code> - coordinate a migration crew with ownership zones (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Coordinate a migration crew with ownership zones in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 85.
```
</details>

<details>
<summary><code>multi-agent-086</code> - orchestrate a translation-plus-glossary crew (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Orchestrate a translation-plus-glossary crew for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 86.
```
</details>

<details>
<summary><code>multi-agent-087</code> - build a map-reduce doc review with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a map-reduce doc review with merge rules for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 87.
```
</details>

<details>
<summary><code>multi-agent-088</code> - run a red-vs-blue review (defensive) with judges (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Run a red-vs-blue review (defensive) with judges for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 88.
```
</details>

<details>
<summary><code>multi-agent-089</code> - orchestrate design+code+QA agents with handoffs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Orchestrate design+code+QA agents with handoffs for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 89.
```
</details>

<details>
<summary><code>multi-agent-090</code> - build a support-triage swarm with escalation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a support-triage swarm with escalation with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 90.
```
</details>

<details>
<summary><code>multi-agent-091</code> - split a research brief across three parallel subagents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Split a research brief across three parallel subagents in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 91.
```
</details>

<details>
<summary><code>multi-agent-092</code> - coordinate a release crew: notes, QA, comms (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Coordinate a release crew: notes, QA, comms for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 92.
```
</details>

<details>
<summary><code>multi-agent-093</code> - design an agent stop/ask/continue policy (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Design an agent stop/ask/continue policy for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 93.
```
</details>

<details>
<summary><code>multi-agent-094</code> - orchestrate a data pipeline: extract, validate, load agents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Orchestrate a data pipeline: extract, validate, load agents for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 94.
```
</details>

<details>
<summary><code>multi-agent-095</code> - run a docs-sync crew across repos (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Run a docs-sync crew across repos for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 95.
```
</details>

<details>
<summary><code>multi-agent-096</code> - build a critic loop: drafter, checker, fixer (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a critic loop: drafter, checker, fixer with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 96.
```
</details>

<details>
<summary><code>multi-agent-097</code> - build a meeting-to-actions pipeline with owners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Build a meeting-to-actions pipeline with owners in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 97.
```
</details>

<details>
<summary><code>multi-agent-098</code> - run competing solution spikes then merge winners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Run competing solution spikes then merge winners for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 98.
```
</details>

<details>
<summary><code>multi-agent-099</code> - coordinate a test-generation swarm per module (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Coordinate a test-generation swarm per module for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 99.
```
</details>

<details>
<summary><code>multi-agent-100</code> - coordinate a migration crew with ownership zones (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Coordinate a migration crew with ownership zones for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 100.
```
</details>

<details>
<summary><code>multi-agent-101</code> - orchestrate a translation-plus-glossary crew (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Orchestrate a translation-plus-glossary crew for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 101.
```
</details>

<details>
<summary><code>multi-agent-102</code> - build a map-reduce doc review with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a map-reduce doc review with merge rules with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 102.
```
</details>

<details>
<summary><code>multi-agent-103</code> - run a red-vs-blue review (defensive) with judges (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Run a red-vs-blue review (defensive) with judges in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 103.
```
</details>

<details>
<summary><code>multi-agent-104</code> - orchestrate design+code+QA agents with handoffs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Orchestrate design+code+QA agents with handoffs for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 104.
```
</details>

<details>
<summary><code>multi-agent-105</code> - build a support-triage swarm with escalation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a support-triage swarm with escalation for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 105.
```
</details>

<details>
<summary><code>multi-agent-106</code> - split a research brief across three parallel subagents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Split a research brief across three parallel subagents for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 106.
```
</details>

<details>
<summary><code>multi-agent-107</code> - coordinate a release crew: notes, QA, comms (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Coordinate a release crew: notes, QA, comms for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 107.
```
</details>

<details>
<summary><code>multi-agent-108</code> - design an agent stop/ask/continue policy (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Design an agent stop/ask/continue policy with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 108.
```
</details>

<details>
<summary><code>multi-agent-109</code> - orchestrate a data pipeline: extract, validate, load agents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Orchestrate a data pipeline: extract, validate, load agents in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 109.
```
</details>

<details>
<summary><code>multi-agent-110</code> - run a docs-sync crew across repos (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Run a docs-sync crew across repos for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 110.
```
</details>

<details>
<summary><code>multi-agent-111</code> - build a critic loop: drafter, checker, fixer (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a critic loop: drafter, checker, fixer for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 111.
```
</details>

<details>
<summary><code>multi-agent-112</code> - build a meeting-to-actions pipeline with owners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Build a meeting-to-actions pipeline with owners for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 112.
```
</details>

<details>
<summary><code>multi-agent-113</code> - run competing solution spikes then merge winners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Run competing solution spikes then merge winners for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 113.
```
</details>

<details>
<summary><code>multi-agent-114</code> - coordinate a test-generation swarm per module (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Coordinate a test-generation swarm per module with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 114.
```
</details>

<details>
<summary><code>multi-agent-115</code> - coordinate a migration crew with ownership zones (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Coordinate a migration crew with ownership zones in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 115.
```
</details>

<details>
<summary><code>multi-agent-116</code> - orchestrate a translation-plus-glossary crew (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Orchestrate a translation-plus-glossary crew for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 116.
```
</details>

<details>
<summary><code>multi-agent-117</code> - build a map-reduce doc review with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a map-reduce doc review with merge rules for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 117.
```
</details>

<details>
<summary><code>multi-agent-118</code> - run a red-vs-blue review (defensive) with judges (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Run a red-vs-blue review (defensive) with judges for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 118.
```
</details>

<details>
<summary><code>multi-agent-119</code> - orchestrate design+code+QA agents with handoffs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Orchestrate design+code+QA agents with handoffs for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 119.
```
</details>

<details>
<summary><code>multi-agent-120</code> - build a support-triage swarm with escalation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a support-triage swarm with escalation with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 120.
```
</details>

<details>
<summary><code>multi-agent-121</code> - split a research brief across three parallel subagents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Split a research brief across three parallel subagents in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 121.
```
</details>

<details>
<summary><code>multi-agent-122</code> - coordinate a release crew: notes, QA, comms (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Coordinate a release crew: notes, QA, comms for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 122.
```
</details>

<details>
<summary><code>multi-agent-123</code> - design an agent stop/ask/continue policy (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Design an agent stop/ask/continue policy for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 123.
```
</details>

<details>
<summary><code>multi-agent-124</code> - orchestrate a data pipeline: extract, validate, load agents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Orchestrate a data pipeline: extract, validate, load agents for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 124.
```
</details>

<details>
<summary><code>multi-agent-125</code> - run a docs-sync crew across repos (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Run a docs-sync crew across repos for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 125.
```
</details>

<details>
<summary><code>multi-agent-126</code> - build a critic loop: drafter, checker, fixer (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a critic loop: drafter, checker, fixer with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 126.
```
</details>

<details>
<summary><code>multi-agent-127</code> - build a meeting-to-actions pipeline with owners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Build a meeting-to-actions pipeline with owners in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 127.
```
</details>

<details>
<summary><code>multi-agent-128</code> - run competing solution spikes then merge winners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Run competing solution spikes then merge winners for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 128.
```
</details>

<details>
<summary><code>multi-agent-129</code> - coordinate a test-generation swarm per module (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Coordinate a test-generation swarm per module for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 129.
```
</details>

<details>
<summary><code>multi-agent-130</code> - coordinate a migration crew with ownership zones (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Coordinate a migration crew with ownership zones for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 130.
```
</details>

<details>
<summary><code>multi-agent-131</code> - orchestrate a translation-plus-glossary crew (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Orchestrate a translation-plus-glossary crew for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 131.
```
</details>

<details>
<summary><code>multi-agent-132</code> - build a map-reduce doc review with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a map-reduce doc review with merge rules with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 132.
```
</details>

<details>
<summary><code>multi-agent-133</code> - run a red-vs-blue review (defensive) with judges (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Run a red-vs-blue review (defensive) with judges in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 133.
```
</details>

<details>
<summary><code>multi-agent-134</code> - orchestrate design+code+QA agents with handoffs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Orchestrate design+code+QA agents with handoffs for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 134.
```
</details>

<details>
<summary><code>multi-agent-135</code> - build a support-triage swarm with escalation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a support-triage swarm with escalation for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 135.
```
</details>

<details>
<summary><code>multi-agent-136</code> - split a research brief across three parallel subagents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Split a research brief across three parallel subagents for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 136.
```
</details>

<details>
<summary><code>multi-agent-137</code> - coordinate a release crew: notes, QA, comms (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Coordinate a release crew: notes, QA, comms for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 137.
```
</details>

<details>
<summary><code>multi-agent-138</code> - design an agent stop/ask/continue policy (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Design an agent stop/ask/continue policy with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 138.
```
</details>

<details>
<summary><code>multi-agent-139</code> - orchestrate a data pipeline: extract, validate, load agents (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Orchestrate a data pipeline: extract, validate, load agents in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 139.
```
</details>

<details>
<summary><code>multi-agent-140</code> - run a docs-sync crew across repos (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Run a docs-sync crew across repos for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 140.
```
</details>

<details>
<summary><code>multi-agent-141</code> - build a critic loop: drafter, checker, fixer (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a critic loop: drafter, checker, fixer for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 141.
```
</details>

<details>
<summary><code>multi-agent-142</code> - build a meeting-to-actions pipeline with owners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Build a meeting-to-actions pipeline with owners for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 142.
```
</details>

<details>
<summary><code>multi-agent-143</code> - run competing solution spikes then merge winners (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Run competing solution spikes then merge winners for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 143.
```
</details>

<details>
<summary><code>multi-agent-144</code> - coordinate a test-generation swarm per module (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Coordinate a test-generation swarm per module with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 144.
```
</details>

<details>
<summary><code>multi-agent-145</code> - coordinate a migration crew with ownership zones (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal agent architect.
Coordinate a migration crew with ownership zones in Codex.
The intended result is an orchestration plan with swimlanes.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 145.
```
</details>

<details>
<summary><code>multi-agent-146</code> - orchestrate a translation-plus-glossary crew (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior orchestrator designer.
Orchestrate a translation-plus-glossary crew for a hackathon.
The intended result is a stop-and-ask policy.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested thinking level: `low`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 146.
```
</details>

<details>
<summary><code>multi-agent-147</code> - build a map-reduce doc review with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert workflow engineer.
Build a map-reduce doc review with merge rules for a classroom demo.
The intended result is a cost/latency estimate.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Use tools where they help; state what evidence you checked before acting.
Suggested thinking level: `medium`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 147.
```
</details>

<details>
<summary><code>multi-agent-148</code> - run a red-vs-blue review (defensive) with judges (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior Codex operator.
Run a red-vs-blue review (defensive) with judges for an enterprise pilot.
The intended result is a handoff template.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested thinking level: `high`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 148.
```
</details>

<details>
<summary><code>multi-agent-149</code> - orchestrate design+code+QA agents with handoffs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a multi-agent systems lead.
Orchestrate design+code+QA agents with handoffs for a startup team.
The intended result is a merge rubric.
Requirements: name when to delegate vs do directly; define each subagent's inputs, outputs, and done
criteria.
Keep a searchable working note so the task survives context compaction.
Suggested thinking level: `xhigh`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 149.
```
</details>

<details>
<summary><code>multi-agent-150</code> - build a support-triage swarm with escalation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior autonomy engineer.
Build a support-triage swarm with escalation with the Responses API.
The intended result is subagent briefs with acceptance criteria.
Requirements: cap parallelism; note rate and cost limits; define conflict resolution when agents
disagree.
Compare against the provided reference and fix the largest gaps first.
Suggested thinking level: `max`.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 150.
```
</details>
