# 🔗 Complex Prompt Chains & Multi-Model Orchestration - 120 copyable Gemini 4 Argon prompts

> Multi-step chains, multi-model routing, validation gates, and compounding-error control.

> Target model: Gemini 4 Argon (`gemini-4-argon`). Sparse MoE with native multimodal (text/image/audio/video). Context 1M. Knowledge cutoff Mar 2026. Strong on knowledge work, finance/legal, cybersecurity defense.

> Safety: defensive / authorized-scope use only. Stop before destructive, irreversible, sending, purchasing, deleting, or permission-changing steps without approval.

**Jump:** [Model index](../../README.md) · [Search all](prompts_index.json)

How to use: click any prompt title to expand it top to bottom, then use the copy icon on the code block.

<details>
<summary><code>prompt-chains-001</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a 5-stage research chain with validation gates for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-002</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a decision chain with option scoring and rationale for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-003</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a cost-optimized chain with model tiering for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-004</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a content pipeline: outline, draft, edit, polish for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-005</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a chain observability spec with traces for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-006</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a data-extraction chain with schema validation for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-007</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a fallback chain when a model fails for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-008</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a code-gen chain: spec, implement, test, review for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-009</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a validation gate that blocks low-confidence outputs for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-010</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a document-QA chain with citation verification for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-011</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-agent research crew with merge rules for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-012</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a chain with self-critique and revision loop for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-013</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a support-triage chain with escalation rules for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-014</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-model router that picks the best model per subtask for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-015</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a translation chain with glossary enforcement for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-016</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a 5-stage research chain with validation gates for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-017</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a decision chain with option scoring and rationale for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-018</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a cost-optimized chain with model tiering for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-019</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a content pipeline: outline, draft, edit, polish for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-020</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a chain observability spec with traces for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-021</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a data-extraction chain with schema validation for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-022</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a fallback chain when a model fails for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-023</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a code-gen chain: spec, implement, test, review for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-024</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a validation gate that blocks low-confidence outputs for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-025</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a document-QA chain with citation verification for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-026</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-agent research crew with merge rules for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-027</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a chain with self-critique and revision loop for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-028</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a support-triage chain with escalation rules for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-029</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-model router that picks the best model per subtask for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-030</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a translation chain with glossary enforcement for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-031</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a 5-stage research chain with validation gates for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-032</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a decision chain with option scoring and rationale for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-033</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a cost-optimized chain with model tiering for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-034</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a content pipeline: outline, draft, edit, polish for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-035</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a chain observability spec with traces for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-036</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a data-extraction chain with schema validation for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-037</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a fallback chain when a model fails for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-038</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a code-gen chain: spec, implement, test, review for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-039</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a validation gate that blocks low-confidence outputs for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-040</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a document-QA chain with citation verification for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-041</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-agent research crew with merge rules for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-042</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a chain with self-critique and revision loop for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-043</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a support-triage chain with escalation rules for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-044</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-model router that picks the best model per subtask for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-045</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a translation chain with glossary enforcement for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-046</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a 5-stage research chain with validation gates for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-047</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a decision chain with option scoring and rationale for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-048</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a cost-optimized chain with model tiering for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-049</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a content pipeline: outline, draft, edit, polish for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-050</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a chain observability spec with traces for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-051</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a data-extraction chain with schema validation for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-052</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a fallback chain when a model fails for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-053</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a code-gen chain: spec, implement, test, review for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-054</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a validation gate that blocks low-confidence outputs for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-055</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a document-QA chain with citation verification for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-056</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-agent research crew with merge rules for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-057</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a chain with self-critique and revision loop for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-058</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a support-triage chain with escalation rules for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-059</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-model router that picks the best model per subtask for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-060</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a translation chain with glossary enforcement for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-061</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a 5-stage research chain with validation gates for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-062</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a decision chain with option scoring and rationale for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-063</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a cost-optimized chain with model tiering for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-064</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a content pipeline: outline, draft, edit, polish for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-065</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a chain observability spec with traces for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-066</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a data-extraction chain with schema validation for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-067</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a fallback chain when a model fails for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-068</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a code-gen chain: spec, implement, test, review for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-069</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a validation gate that blocks low-confidence outputs for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-070</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a document-QA chain with citation verification for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-071</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-agent research crew with merge rules for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-072</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a chain with self-critique and revision loop for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-073</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a support-triage chain with escalation rules for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-074</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-model router that picks the best model per subtask for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-075</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a translation chain with glossary enforcement for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-076</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a 5-stage research chain with validation gates for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-077</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a decision chain with option scoring and rationale for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-078</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a cost-optimized chain with model tiering for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-079</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a content pipeline: outline, draft, edit, polish for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-080</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a chain observability spec with traces for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-081</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a data-extraction chain with schema validation for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-082</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a fallback chain when a model fails for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-083</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a code-gen chain: spec, implement, test, review for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-084</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a validation gate that blocks low-confidence outputs for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-085</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a document-QA chain with citation verification for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-086</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-agent research crew with merge rules for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-087</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a chain with self-critique and revision loop for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-088</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a support-triage chain with escalation rules for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-089</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-model router that picks the best model per subtask for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-090</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a translation chain with glossary enforcement for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-091</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a 5-stage research chain with validation gates for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-092</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a decision chain with option scoring and rationale for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-093</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a cost-optimized chain with model tiering for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-094</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a content pipeline: outline, draft, edit, polish for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-095</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a chain observability spec with traces for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-096</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a data-extraction chain with schema validation for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-097</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a fallback chain when a model fails for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-098</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a code-gen chain: spec, implement, test, review for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-099</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a validation gate that blocks low-confidence outputs for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-100</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a document-QA chain with citation verification for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-101</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-agent research crew with merge rules for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-102</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a chain with self-critique and revision loop for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-103</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a support-triage chain with escalation rules for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-104</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-model router that picks the best model per subtask for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-105</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a translation chain with glossary enforcement for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-106</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a 5-stage research chain with validation gates for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-107</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a decision chain with option scoring and rationale for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-108</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a cost-optimized chain with model tiering for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-109</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a content pipeline: outline, draft, edit, polish for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-110</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a chain observability spec with traces for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-111</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a data-extraction chain with schema validation for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-112</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a fallback chain when a model fails for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-113</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a code-gen chain: spec, implement, test, review for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-114</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a validation gate that blocks low-confidence outputs for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-115</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a document-QA chain with citation verification for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-116</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-agent research crew with merge rules for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-117</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a chain with self-critique and revision loop for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-118</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a support-triage chain with escalation rules for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-119</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-model router that picks the best model per subtask for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-120</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a translation chain with glossary enforcement for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-121</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a 5-stage research chain with validation gates for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-122</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a decision chain with option scoring and rationale for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-123</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a cost-optimized chain with model tiering for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-124</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a content pipeline: outline, draft, edit, polish for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-125</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a chain observability spec with traces for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-126</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a data-extraction chain with schema validation for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-127</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a fallback chain when a model fails for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-128</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a code-gen chain: spec, implement, test, review for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-129</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a validation gate that blocks low-confidence outputs for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-130</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a document-QA chain with citation verification for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-131</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-agent research crew with merge rules for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-132</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a chain with self-critique and revision loop for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-133</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a support-triage chain with escalation rules for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-134</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-model router that picks the best model per subtask for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-135</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a translation chain with glossary enforcement for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-136</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a 5-stage research chain with validation gates for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-137</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a decision chain with option scoring and rationale for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-138</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a cost-optimized chain with model tiering for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-139</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a content pipeline: outline, draft, edit, polish for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-140</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a chain observability spec with traces for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-141</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a data-extraction chain with schema validation for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-142</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a fallback chain when a model fails for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-143</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a code-gen chain: spec, implement, test, review for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-144</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a validation gate that blocks low-confidence outputs for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>prompt-chains-145</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a document-QA chain with citation verification for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>prompt-chains-146</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-agent research crew with merge rules for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>prompt-chains-147</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a chain with self-critique and revision loop for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>prompt-chains-148</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a support-triage chain with escalation rules for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>prompt-chains-149</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-model router that picks the best model per subtask for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>prompt-chains-150</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a translation chain with glossary enforcement for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
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

<details>
<summary><code>prompt-chains-151</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a 5-stage research chain with validation gates for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 151.
```
</details>

<details>
<summary><code>prompt-chains-152</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a decision chain with option scoring and rationale for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 152.
```
</details>

<details>
<summary><code>prompt-chains-153</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a cost-optimized chain with model tiering for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
Variant focus 153.
```
</details>

<details>
<summary><code>prompt-chains-154</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a content pipeline: outline, draft, edit, polish for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 154.
```
</details>

<details>
<summary><code>prompt-chains-155</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a chain observability spec with traces for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 155.
```
</details>

<details>
<summary><code>prompt-chains-156</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a data-extraction chain with schema validation for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 156.
```
</details>

<details>
<summary><code>prompt-chains-157</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a fallback chain when a model fails for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 157.
```
</details>

<details>
<summary><code>prompt-chains-158</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a code-gen chain: spec, implement, test, review for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 158.
```
</details>

<details>
<summary><code>prompt-chains-159</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a validation gate that blocks low-confidence outputs for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 159.
```
</details>

<details>
<summary><code>prompt-chains-160</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a document-QA chain with citation verification for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
Variant focus 160.
```
</details>

<details>
<summary><code>prompt-chains-161</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-agent research crew with merge rules for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 161.
```
</details>

<details>
<summary><code>prompt-chains-162</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a chain with self-critique and revision loop for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 162.
```
</details>

<details>
<summary><code>prompt-chains-163</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a support-triage chain with escalation rules for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 163.
```
</details>

<details>
<summary><code>prompt-chains-164</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-model router that picks the best model per subtask for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 164.
```
</details>

<details>
<summary><code>prompt-chains-165</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a translation chain with glossary enforcement for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
Variant focus 165.
```
</details>

<details>
<summary><code>prompt-chains-166</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a 5-stage research chain with validation gates for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 166.
```
</details>

<details>
<summary><code>prompt-chains-167</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a decision chain with option scoring and rationale for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 167.
```
</details>

<details>
<summary><code>prompt-chains-168</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a cost-optimized chain with model tiering for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 168.
```
</details>

<details>
<summary><code>prompt-chains-169</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a content pipeline: outline, draft, edit, polish for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 169.
```
</details>

<details>
<summary><code>prompt-chains-170</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a chain observability spec with traces for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 170.
```
</details>

<details>
<summary><code>prompt-chains-171</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a data-extraction chain with schema validation for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 171.
```
</details>

<details>
<summary><code>prompt-chains-172</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a fallback chain when a model fails for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 172.
```
</details>

<details>
<summary><code>prompt-chains-173</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a code-gen chain: spec, implement, test, review for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 173.
```
</details>

<details>
<summary><code>prompt-chains-174</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a validation gate that blocks low-confidence outputs for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 174.
```
</details>

<details>
<summary><code>prompt-chains-175</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a document-QA chain with citation verification for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 175.
```
</details>

<details>
<summary><code>prompt-chains-176</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-agent research crew with merge rules for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 176.
```
</details>

<details>
<summary><code>prompt-chains-177</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a chain with self-critique and revision loop for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 177.
```
</details>

<details>
<summary><code>prompt-chains-178</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a support-triage chain with escalation rules for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
Variant focus 178.
```
</details>

<details>
<summary><code>prompt-chains-179</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-model router that picks the best model per subtask for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 179.
```
</details>

<details>
<summary><code>prompt-chains-180</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a translation chain with glossary enforcement for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 180.
```
</details>

<details>
<summary><code>prompt-chains-181</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a 5-stage research chain with validation gates for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 181.
```
</details>

<details>
<summary><code>prompt-chains-182</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a decision chain with option scoring and rationale for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 182.
```
</details>

<details>
<summary><code>prompt-chains-183</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a cost-optimized chain with model tiering for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
Variant focus 183.
```
</details>

<details>
<summary><code>prompt-chains-184</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a content pipeline: outline, draft, edit, polish for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 184.
```
</details>

<details>
<summary><code>prompt-chains-185</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a chain observability spec with traces for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 185.
```
</details>

<details>
<summary><code>prompt-chains-186</code> - create a data-extraction chain with schema validation (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a data-extraction chain with schema validation for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 186.
```
</details>

<details>
<summary><code>prompt-chains-187</code> - design a fallback chain when a model fails (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a fallback chain when a model fails for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 187.
```
</details>

<details>
<summary><code>prompt-chains-188</code> - build a code-gen chain: spec, implement, test, review (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a code-gen chain: spec, implement, test, review for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 188.
```
</details>

<details>
<summary><code>prompt-chains-189</code> - create a validation gate that blocks low-confidence outputs (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a validation gate that blocks low-confidence outputs for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 189.
```
</details>

<details>
<summary><code>prompt-chains-190</code> - design a document-QA chain with citation verification (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a document-QA chain with citation verification for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
Variant focus 190.
```
</details>

<details>
<summary><code>prompt-chains-191</code> - build a multi-agent research crew with merge rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a multi-agent research crew with merge rules for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 191.
```
</details>

<details>
<summary><code>prompt-chains-192</code> - create a chain with self-critique and revision loop (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a chain with self-critique and revision loop for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 192.
```
</details>

<details>
<summary><code>prompt-chains-193</code> - design a support-triage chain with escalation rules (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a support-triage chain with escalation rules for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 193.
```
</details>

<details>
<summary><code>prompt-chains-194</code> - build a multi-model router that picks the best model per subtask (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a multi-model router that picks the best model per subtask for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 194.
```
</details>

<details>
<summary><code>prompt-chains-195</code> - create a translation chain with glossary enforcement (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert multi-model router.
Create a translation chain with glossary enforcement for a classroom.
The intended result is a cost/latency estimate.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Use tools where they help; state what evidence you checked before acting.
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
Variant focus 195.
```
</details>

<details>
<summary><code>prompt-chains-196</code> - design a 5-stage research chain with validation gates (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior workflow engineer.
Design a 5-stage research chain with validation gates for a research lab.
The intended result is a trace schema.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 196.
```
</details>

<details>
<summary><code>prompt-chains-197</code> - build a decision chain with option scoring and rationale (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as an expert validation engineer.
Build a decision chain with option scoring and rationale for an enterprise.
The intended result is a validation gate design.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Keep a searchable working note so the task survives context compaction.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 197.
```
</details>

<details>
<summary><code>prompt-chains-198</code> - create a cost-optimized chain with model tiering (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior AI systems architect.
Create a cost-optimized chain with model tiering for a startup.
The intended result is a router policy.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Compare against the provided reference and fix the largest gaps first.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 198.
```
</details>

<details>
<summary><code>prompt-chains-199</code> - design a content pipeline: outline, draft, edit, polish (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a principal prompt architect.
Design a content pipeline: outline, draft, edit, polish for a production API.
The intended result is a chain spec with stages.
Requirements: cap chain length; note latency and cost; validate each stage before passing forward.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 199.
```
</details>

<details>
<summary><code>prompt-chains-200</code> - build a chain observability spec with traces (click to expand)</summary>

```text
Target model: Gemini 4 Argon (gemini-4-argon).
Act as a senior chain designer.
Build a chain observability spec with traces for open source.
The intended result is a test plan.
Requirements: keep stages idempotent where possible; log inputs/outputs for audit.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Sparse MoE with native multimodal (text/image/audio/video).
Context 1M.
Knowledge cutoff Mar 2026.
Strong on knowledge work, finance/legal, cybersecurity defense.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 200.
```
</details>
