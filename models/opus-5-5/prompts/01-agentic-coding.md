# 💻 Agentic Coding - 120 copyable Claude Opus 5.5 prompts

> Long-horizon coding tasks, refactors, Codex/Copilot workflows with verification proportional to risk.

> Target model: Claude Opus 5.5 (`claude-opus-5-5`). Adaptive thinking is always on; steer depth with the effort parameter (default medium). Context 1M, max output 128K. $4/$20 per MTok. Knowledge cutoff Jun 2026. Cache reads 5% of base input.

> Safety: defensive / authorized-scope use only. Stop before destructive, irreversible, sending, purchasing, deleting, or permission-changing steps without approval.

**Jump:** [Model index](../../README.md) · [Search all](prompts_index.json)

How to use: click any prompt title to expand it top to bottom, then use the copy icon on the code block.

<details>
<summary><code>agentic-coding-001</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>agentic-coding-002</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an e-commerce
platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>agentic-coding-003</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Create a feature-flag system with targeting rules and audit log for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>agentic-coding-004</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Create a CLI tool with config files, help text, and shell completions for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>agentic-coding-005</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Build a file-upload pipeline with virus-scan hooks and size limits for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>agentic-coding-006</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Optimize a slow database query path and prove the speedup with benchmarks for an enterprise internal
tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>agentic-coding-007</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Write a migration script with dry-run, rollback, and data validation for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>agentic-coding-008</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Add role-based access control to an existing API with tests for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>agentic-coding-009</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Add structured logging, tracing, and health checks to a service for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>agentic-coding-010</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Implement a background job queue with retries, idempotency, and observability for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>agentic-coding-011</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Implement pagination, filtering, and sorting for a list API for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>agentic-coding-012</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Migrate a callback-based flow to async/await with full type safety for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>agentic-coding-013</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Convert a monolith handler into testable services with dependency injection for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>agentic-coding-014</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Refactor a tangled module into clean layers without changing behavior for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>agentic-coding-015</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Build a webhook receiver with signature verification and replay protection for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>agentic-coding-016</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>agentic-coding-017</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an open-source
library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>agentic-coding-018</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Create a feature-flag system with targeting rules and audit log for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>agentic-coding-019</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Create a CLI tool with config files, help text, and shell completions for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>agentic-coding-020</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Build a file-upload pipeline with virus-scan hooks and size limits for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>agentic-coding-021</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Optimize a slow database query path and prove the speedup with benchmarks for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>agentic-coding-022</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Write a migration script with dry-run, rollback, and data validation for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>agentic-coding-023</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Add role-based access control to an existing API with tests for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>agentic-coding-024</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Add structured logging, tracing, and health checks to a service for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>agentic-coding-025</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Implement a background job queue with retries, idempotency, and observability for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>agentic-coding-026</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Implement pagination, filtering, and sorting for a list API for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>agentic-coding-027</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Migrate a callback-based flow to async/await with full type safety for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>agentic-coding-028</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Convert a monolith handler into testable services with dependency injection for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>agentic-coding-029</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Refactor a tangled module into clean layers without changing behavior for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>agentic-coding-030</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Build a webhook receiver with signature verification and replay protection for an enterprise
internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>agentic-coding-031</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 31.
```
</details>

<details>
<summary><code>agentic-coding-032</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an e-commerce
platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 32.
```
</details>

<details>
<summary><code>agentic-coding-033</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Create a feature-flag system with targeting rules and audit log for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-034</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Create a CLI tool with config files, help text, and shell completions for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 34.
```
</details>

<details>
<summary><code>agentic-coding-035</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Build a file-upload pipeline with virus-scan hooks and size limits for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 35.
```
</details>

<details>
<summary><code>agentic-coding-036</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Optimize a slow database query path and prove the speedup with benchmarks for an enterprise internal
tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 36.
```
</details>

<details>
<summary><code>agentic-coding-037</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Write a migration script with dry-run, rollback, and data validation for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 37.
```
</details>

<details>
<summary><code>agentic-coding-038</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Add role-based access control to an existing API with tests for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 38.
```
</details>

<details>
<summary><code>agentic-coding-039</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Add structured logging, tracing, and health checks to a service for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 39.
```
</details>

<details>
<summary><code>agentic-coding-040</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Implement a background job queue with retries, idempotency, and observability for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-041</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Implement pagination, filtering, and sorting for a list API for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 41.
```
</details>

<details>
<summary><code>agentic-coding-042</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Migrate a callback-based flow to async/await with full type safety for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 42.
```
</details>

<details>
<summary><code>agentic-coding-043</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Convert a monolith handler into testable services with dependency injection for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 43.
```
</details>

<details>
<summary><code>agentic-coding-044</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Refactor a tangled module into clean layers without changing behavior for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 44.
```
</details>

<details>
<summary><code>agentic-coding-045</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Build a webhook receiver with signature verification and replay protection for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-046</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 46.
```
</details>

<details>
<summary><code>agentic-coding-047</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an open-source
library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 47.
```
</details>

<details>
<summary><code>agentic-coding-048</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Create a feature-flag system with targeting rules and audit log for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 48.
```
</details>

<details>
<summary><code>agentic-coding-049</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Create a CLI tool with config files, help text, and shell completions for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 49.
```
</details>

<details>
<summary><code>agentic-coding-050</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Build a file-upload pipeline with virus-scan hooks and size limits for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 50.
```
</details>

<details>
<summary><code>agentic-coding-051</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Optimize a slow database query path and prove the speedup with benchmarks for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 51.
```
</details>

<details>
<summary><code>agentic-coding-052</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Write a migration script with dry-run, rollback, and data validation for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 52.
```
</details>

<details>
<summary><code>agentic-coding-053</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Add role-based access control to an existing API with tests for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 53.
```
</details>

<details>
<summary><code>agentic-coding-054</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Add structured logging, tracing, and health checks to a service for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 54.
```
</details>

<details>
<summary><code>agentic-coding-055</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Implement a background job queue with retries, idempotency, and observability for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 55.
```
</details>

<details>
<summary><code>agentic-coding-056</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Implement pagination, filtering, and sorting for a list API for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 56.
```
</details>

<details>
<summary><code>agentic-coding-057</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Migrate a callback-based flow to async/await with full type safety for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 57.
```
</details>

<details>
<summary><code>agentic-coding-058</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Convert a monolith handler into testable services with dependency injection for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-059</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Refactor a tangled module into clean layers without changing behavior for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 59.
```
</details>

<details>
<summary><code>agentic-coding-060</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Build a webhook receiver with signature verification and replay protection for an enterprise
internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 60.
```
</details>

<details>
<summary><code>agentic-coding-061</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 61.
```
</details>

<details>
<summary><code>agentic-coding-062</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an e-commerce
platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 62.
```
</details>

<details>
<summary><code>agentic-coding-063</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Create a feature-flag system with targeting rules and audit log for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-064</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Create a CLI tool with config files, help text, and shell completions for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 64.
```
</details>

<details>
<summary><code>agentic-coding-065</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Build a file-upload pipeline with virus-scan hooks and size limits for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 65.
```
</details>

<details>
<summary><code>agentic-coding-066</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Optimize a slow database query path and prove the speedup with benchmarks for an enterprise internal
tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 66.
```
</details>

<details>
<summary><code>agentic-coding-067</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Write a migration script with dry-run, rollback, and data validation for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 67.
```
</details>

<details>
<summary><code>agentic-coding-068</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Add role-based access control to an existing API with tests for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 68.
```
</details>

<details>
<summary><code>agentic-coding-069</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Add structured logging, tracing, and health checks to a service for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 69.
```
</details>

<details>
<summary><code>agentic-coding-070</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Implement a background job queue with retries, idempotency, and observability for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-071</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Implement pagination, filtering, and sorting for a list API for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 71.
```
</details>

<details>
<summary><code>agentic-coding-072</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Migrate a callback-based flow to async/await with full type safety for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 72.
```
</details>

<details>
<summary><code>agentic-coding-073</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Convert a monolith handler into testable services with dependency injection for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 73.
```
</details>

<details>
<summary><code>agentic-coding-074</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Refactor a tangled module into clean layers without changing behavior for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 74.
```
</details>

<details>
<summary><code>agentic-coding-075</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Build a webhook receiver with signature verification and replay protection for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-076</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 76.
```
</details>

<details>
<summary><code>agentic-coding-077</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an open-source
library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 77.
```
</details>

<details>
<summary><code>agentic-coding-078</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Create a feature-flag system with targeting rules and audit log for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 78.
```
</details>

<details>
<summary><code>agentic-coding-079</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Create a CLI tool with config files, help text, and shell completions for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 79.
```
</details>

<details>
<summary><code>agentic-coding-080</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Build a file-upload pipeline with virus-scan hooks and size limits for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 80.
```
</details>

<details>
<summary><code>agentic-coding-081</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Optimize a slow database query path and prove the speedup with benchmarks for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 81.
```
</details>

<details>
<summary><code>agentic-coding-082</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Write a migration script with dry-run, rollback, and data validation for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 82.
```
</details>

<details>
<summary><code>agentic-coding-083</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Add role-based access control to an existing API with tests for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 83.
```
</details>

<details>
<summary><code>agentic-coding-084</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Add structured logging, tracing, and health checks to a service for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 84.
```
</details>

<details>
<summary><code>agentic-coding-085</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Implement a background job queue with retries, idempotency, and observability for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 85.
```
</details>

<details>
<summary><code>agentic-coding-086</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Implement pagination, filtering, and sorting for a list API for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 86.
```
</details>

<details>
<summary><code>agentic-coding-087</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Migrate a callback-based flow to async/await with full type safety for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 87.
```
</details>

<details>
<summary><code>agentic-coding-088</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Convert a monolith handler into testable services with dependency injection for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-089</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Refactor a tangled module into clean layers without changing behavior for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 89.
```
</details>

<details>
<summary><code>agentic-coding-090</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Build a webhook receiver with signature verification and replay protection for an enterprise
internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 90.
```
</details>

<details>
<summary><code>agentic-coding-091</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 91.
```
</details>

<details>
<summary><code>agentic-coding-092</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an e-commerce
platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 92.
```
</details>

<details>
<summary><code>agentic-coding-093</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Create a feature-flag system with targeting rules and audit log for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-094</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Create a CLI tool with config files, help text, and shell completions for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 94.
```
</details>

<details>
<summary><code>agentic-coding-095</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Build a file-upload pipeline with virus-scan hooks and size limits for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 95.
```
</details>

<details>
<summary><code>agentic-coding-096</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Optimize a slow database query path and prove the speedup with benchmarks for an enterprise internal
tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 96.
```
</details>

<details>
<summary><code>agentic-coding-097</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Write a migration script with dry-run, rollback, and data validation for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 97.
```
</details>

<details>
<summary><code>agentic-coding-098</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Add role-based access control to an existing API with tests for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 98.
```
</details>

<details>
<summary><code>agentic-coding-099</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Add structured logging, tracing, and health checks to a service for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 99.
```
</details>

<details>
<summary><code>agentic-coding-100</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Implement a background job queue with retries, idempotency, and observability for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-101</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Implement pagination, filtering, and sorting for a list API for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 101.
```
</details>

<details>
<summary><code>agentic-coding-102</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Migrate a callback-based flow to async/await with full type safety for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 102.
```
</details>

<details>
<summary><code>agentic-coding-103</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Convert a monolith handler into testable services with dependency injection for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 103.
```
</details>

<details>
<summary><code>agentic-coding-104</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Refactor a tangled module into clean layers without changing behavior for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 104.
```
</details>

<details>
<summary><code>agentic-coding-105</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Build a webhook receiver with signature verification and replay protection for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-106</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 106.
```
</details>

<details>
<summary><code>agentic-coding-107</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an open-source
library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 107.
```
</details>

<details>
<summary><code>agentic-coding-108</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Create a feature-flag system with targeting rules and audit log for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 108.
```
</details>

<details>
<summary><code>agentic-coding-109</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Create a CLI tool with config files, help text, and shell completions for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 109.
```
</details>

<details>
<summary><code>agentic-coding-110</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Build a file-upload pipeline with virus-scan hooks and size limits for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 110.
```
</details>

<details>
<summary><code>agentic-coding-111</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Optimize a slow database query path and prove the speedup with benchmarks for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 111.
```
</details>

<details>
<summary><code>agentic-coding-112</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Write a migration script with dry-run, rollback, and data validation for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 112.
```
</details>

<details>
<summary><code>agentic-coding-113</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Add role-based access control to an existing API with tests for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 113.
```
</details>

<details>
<summary><code>agentic-coding-114</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Add structured logging, tracing, and health checks to a service for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 114.
```
</details>

<details>
<summary><code>agentic-coding-115</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Implement a background job queue with retries, idempotency, and observability for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 115.
```
</details>

<details>
<summary><code>agentic-coding-116</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Implement pagination, filtering, and sorting for a list API for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 116.
```
</details>

<details>
<summary><code>agentic-coding-117</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Migrate a callback-based flow to async/await with full type safety for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 117.
```
</details>

<details>
<summary><code>agentic-coding-118</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Convert a monolith handler into testable services with dependency injection for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-119</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Refactor a tangled module into clean layers without changing behavior for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 119.
```
</details>

<details>
<summary><code>agentic-coding-120</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Build a webhook receiver with signature verification and replay protection for an enterprise
internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 120.
```
</details>

<details>
<summary><code>agentic-coding-121</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 121.
```
</details>

<details>
<summary><code>agentic-coding-122</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an e-commerce
platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 122.
```
</details>

<details>
<summary><code>agentic-coding-123</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Create a feature-flag system with targeting rules and audit log for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-124</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Create a CLI tool with config files, help text, and shell completions for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 124.
```
</details>

<details>
<summary><code>agentic-coding-125</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Build a file-upload pipeline with virus-scan hooks and size limits for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 125.
```
</details>

<details>
<summary><code>agentic-coding-126</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Optimize a slow database query path and prove the speedup with benchmarks for an enterprise internal
tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 126.
```
</details>

<details>
<summary><code>agentic-coding-127</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Write a migration script with dry-run, rollback, and data validation for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 127.
```
</details>

<details>
<summary><code>agentic-coding-128</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Add role-based access control to an existing API with tests for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 128.
```
</details>

<details>
<summary><code>agentic-coding-129</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Add structured logging, tracing, and health checks to a service for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 129.
```
</details>

<details>
<summary><code>agentic-coding-130</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Implement a background job queue with retries, idempotency, and observability for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-131</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Implement pagination, filtering, and sorting for a list API for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 131.
```
</details>

<details>
<summary><code>agentic-coding-132</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Migrate a callback-based flow to async/await with full type safety for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 132.
```
</details>

<details>
<summary><code>agentic-coding-133</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Convert a monolith handler into testable services with dependency injection for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 133.
```
</details>

<details>
<summary><code>agentic-coding-134</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Refactor a tangled module into clean layers without changing behavior for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 134.
```
</details>

<details>
<summary><code>agentic-coding-135</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Build a webhook receiver with signature verification and replay protection for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-136</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 136.
```
</details>

<details>
<summary><code>agentic-coding-137</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an open-source
library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 137.
```
</details>

<details>
<summary><code>agentic-coding-138</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Create a feature-flag system with targeting rules and audit log for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 138.
```
</details>

<details>
<summary><code>agentic-coding-139</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Create a CLI tool with config files, help text, and shell completions for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 139.
```
</details>

<details>
<summary><code>agentic-coding-140</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Build a file-upload pipeline with virus-scan hooks and size limits for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 140.
```
</details>

<details>
<summary><code>agentic-coding-141</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Optimize a slow database query path and prove the speedup with benchmarks for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 141.
```
</details>

<details>
<summary><code>agentic-coding-142</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Write a migration script with dry-run, rollback, and data validation for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 142.
```
</details>

<details>
<summary><code>agentic-coding-143</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Add role-based access control to an existing API with tests for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 143.
```
</details>

<details>
<summary><code>agentic-coding-144</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Add structured logging, tracing, and health checks to a service for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 144.
```
</details>

<details>
<summary><code>agentic-coding-145</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Implement a background job queue with retries, idempotency, and observability for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 145.
```
</details>

<details>
<summary><code>agentic-coding-146</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Implement pagination, filtering, and sorting for a list API for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 146.
```
</details>

<details>
<summary><code>agentic-coding-147</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Migrate a callback-based flow to async/await with full type safety for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 147.
```
</details>

<details>
<summary><code>agentic-coding-148</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Convert a monolith handler into testable services with dependency injection for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-149</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Refactor a tangled module into clean layers without changing behavior for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 149.
```
</details>

<details>
<summary><code>agentic-coding-150</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Build a webhook receiver with signature verification and replay protection for an enterprise
internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 150.
```
</details>

<details>
<summary><code>agentic-coding-151</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 151.
```
</details>

<details>
<summary><code>agentic-coding-152</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an e-commerce
platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 152.
```
</details>

<details>
<summary><code>agentic-coding-153</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Create a feature-flag system with targeting rules and audit log for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-154</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Create a CLI tool with config files, help text, and shell completions for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 154.
```
</details>

<details>
<summary><code>agentic-coding-155</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Build a file-upload pipeline with virus-scan hooks and size limits for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 155.
```
</details>

<details>
<summary><code>agentic-coding-156</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Optimize a slow database query path and prove the speedup with benchmarks for an enterprise internal
tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 156.
```
</details>

<details>
<summary><code>agentic-coding-157</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Write a migration script with dry-run, rollback, and data validation for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 157.
```
</details>

<details>
<summary><code>agentic-coding-158</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Add role-based access control to an existing API with tests for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 158.
```
</details>

<details>
<summary><code>agentic-coding-159</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Add structured logging, tracing, and health checks to a service for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 159.
```
</details>

<details>
<summary><code>agentic-coding-160</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Implement a background job queue with retries, idempotency, and observability for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-161</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Implement pagination, filtering, and sorting for a list API for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 161.
```
</details>

<details>
<summary><code>agentic-coding-162</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Migrate a callback-based flow to async/await with full type safety for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 162.
```
</details>

<details>
<summary><code>agentic-coding-163</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Convert a monolith handler into testable services with dependency injection for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 163.
```
</details>

<details>
<summary><code>agentic-coding-164</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Refactor a tangled module into clean layers without changing behavior for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 164.
```
</details>

<details>
<summary><code>agentic-coding-165</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Build a webhook receiver with signature verification and replay protection for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-166</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 166.
```
</details>

<details>
<summary><code>agentic-coding-167</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an open-source
library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 167.
```
</details>

<details>
<summary><code>agentic-coding-168</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Create a feature-flag system with targeting rules and audit log for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 168.
```
</details>

<details>
<summary><code>agentic-coding-169</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Create a CLI tool with config files, help text, and shell completions for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 169.
```
</details>

<details>
<summary><code>agentic-coding-170</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Build a file-upload pipeline with virus-scan hooks and size limits for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 170.
```
</details>

<details>
<summary><code>agentic-coding-171</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Optimize a slow database query path and prove the speedup with benchmarks for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 171.
```
</details>

<details>
<summary><code>agentic-coding-172</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Write a migration script with dry-run, rollback, and data validation for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 172.
```
</details>

<details>
<summary><code>agentic-coding-173</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Add role-based access control to an existing API with tests for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 173.
```
</details>

<details>
<summary><code>agentic-coding-174</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Add structured logging, tracing, and health checks to a service for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 174.
```
</details>

<details>
<summary><code>agentic-coding-175</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Implement a background job queue with retries, idempotency, and observability for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 175.
```
</details>

<details>
<summary><code>agentic-coding-176</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Implement pagination, filtering, and sorting for a list API for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 176.
```
</details>

<details>
<summary><code>agentic-coding-177</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Migrate a callback-based flow to async/await with full type safety for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 177.
```
</details>

<details>
<summary><code>agentic-coding-178</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Convert a monolith handler into testable services with dependency injection for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-179</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Refactor a tangled module into clean layers without changing behavior for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 179.
```
</details>

<details>
<summary><code>agentic-coding-180</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Build a webhook receiver with signature verification and replay protection for an enterprise
internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 180.
```
</details>

<details>
<summary><code>agentic-coding-181</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 181.
```
</details>

<details>
<summary><code>agentic-coding-182</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an e-commerce
platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 182.
```
</details>

<details>
<summary><code>agentic-coding-183</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Create a feature-flag system with targeting rules and audit log for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-184</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Create a CLI tool with config files, help text, and shell completions for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 184.
```
</details>

<details>
<summary><code>agentic-coding-185</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Build a file-upload pipeline with virus-scan hooks and size limits for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 185.
```
</details>

<details>
<summary><code>agentic-coding-186</code> - optimize a slow database query path and prove the speedup with benchmark (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Optimize a slow database query path and prove the speedup with benchmarks for an enterprise internal
tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 186.
```
</details>

<details>
<summary><code>agentic-coding-187</code> - write a migration script with dry-run, rollback, and data validation (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Write a migration script with dry-run, rollback, and data validation for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 187.
```
</details>

<details>
<summary><code>agentic-coding-188</code> - add role-based access control to an existing API with tests (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Add role-based access control to an existing API with tests for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 188.
```
</details>

<details>
<summary><code>agentic-coding-189</code> - add structured logging, tracing, and health checks to a service (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Add structured logging, tracing, and health checks to a service for a healthcare data service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 189.
```
</details>

<details>
<summary><code>agentic-coding-190</code> - implement a background job queue with retries, idempotency, and observab (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Implement a background job queue with retries, idempotency, and observability for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-191</code> - implement pagination, filtering, and sorting for a list API (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Implement pagination, filtering, and sorting for a list API for an open-source library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 191.
```
</details>

<details>
<summary><code>agentic-coding-192</code> - migrate a callback-based flow to async/await with full type safety (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Migrate a callback-based flow to async/await with full type safety for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 192.
```
</details>

<details>
<summary><code>agentic-coding-193</code> - convert a monolith handler into testable services with dependency inject (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Convert a monolith handler into testable services with dependency injection for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 193.
```
</details>

<details>
<summary><code>agentic-coding-194</code> - refactor a tangled module into clean layers without changing behavior (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Refactor a tangled module into clean layers without changing behavior for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 194.
```
</details>

<details>
<summary><code>agentic-coding-195</code> - build a webhook receiver with signature verification and replay protecti (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior backend engineer.
Build a webhook receiver with signature verification and replay protection for a healthcare data
service.
The intended result is implementation with before/after benchmarks in a table.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Use tools where they help; state what evidence you checked before acting.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
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
<summary><code>agentic-coding-196</code> - build a REST endpoint with validation, error handling, and OpenAPI docs (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a staff full-stack developer.
Build a REST endpoint with validation, error handling, and OpenAPI docs for a fintech backend.
The intended result is code plus a review checklist of risks and mitigations.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Suggested reasoning effort: `low`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 196.
```
</details>

<details>
<summary><code>agentic-coding-197</code> - harden an auth flow against OWASP Top 10 issues and document the threat  (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior platform engineer.
Harden an auth flow against OWASP Top 10 issues and document the threat model for an open-source
library.
The intended result is production-ready code with README usage section.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Keep a searchable working note so the task survives context compaction.
Suggested reasoning effort: `medium`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 197.
```
</details>

<details>
<summary><code>agentic-coding-198</code> - create a feature-flag system with targeting rules and audit log (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert code reviewer.
Create a feature-flag system with targeting rules and audit log for an enterprise internal tool.
The intended result is a unified diff with a file-by-file change summary.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Compare against the provided reference and fix the largest gaps first.
Suggested reasoning effort: `high`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 198.
```
</details>

<details>
<summary><code>agentic-coding-199</code> - create a CLI tool with config files, help text, and shell completions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior staff engineer.
Create a CLI tool with config files, help text, and shell completions for a SaaS startup.
The intended result is a working implementation plus a short test report.
Requirements: reuse existing project patterns; no new dependencies without justification; keep the
diff minimal and reversible; explain every new abstraction.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Suggested reasoning effort: `xhigh`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 199.
```
</details>

<details>
<summary><code>agentic-coding-200</code> - build a file-upload pipeline with virus-scan hooks and size limits (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a principal software architect.
Build a file-upload pipeline with virus-scan hooks and size limits for an e-commerce platform.
The intended result is code plus rollback instructions.
Requirements: preserve backward compatibility for existing API consumers; optimize for readability
over cleverness; add docstrings for public APIs.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Suggested reasoning effort: `max`.
Adaptive thinking is always on; steer depth with the effort parameter (default medium).
Context 1M, max output 128K.
$4/$20 per MTok.
Knowledge cutoff Jun 2026.
Cache reads 5% of base input.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 200.
```
</details>
