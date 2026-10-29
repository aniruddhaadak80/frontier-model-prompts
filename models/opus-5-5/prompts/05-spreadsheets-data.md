# 📊 Spreadsheets & Data Wrangling - 120 copyable Claude Opus 5.5 prompts

> Excel/Sheets models, cleaning recipes, and reconciliation flows.

> Target model: Claude Opus 5.5 (`claude-opus-5-5`). Adaptive thinking is always on; steer depth with the effort parameter (default medium). Context 1M, max output 128K. $4/$20 per MTok. Knowledge cutoff Jun 2026. Cache reads 5% of base input.

> Safety: defensive / authorized-scope use only. Stop before destructive, irreversible, sending, purchasing, deleting, or permission-changing steps without approval.

**Jump:** [Model index](../../README.md) · [Search all](prompts_index.json)

How to use: click any prompt title to expand it top to bottom, then use the copy icon on the code block.

<details>
<summary><code>spreadsheets-data-001</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Reconcile two transaction exports and isolate mismatches for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-002</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a hiring pipeline funnel with conversion rates for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-003</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a data-entry template with validation rules for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-004</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build an inventory reorder sheet with lead-time math for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-005</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a marketing attribution sheet with UTM hygiene checks for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-006</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a commission model with caps and accelerators for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-007</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Create a loan amortization schedule with extra-payment scenarios for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-008</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a cohort retention table from raw events for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-009</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a capacity plan from velocity and leave data for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-010</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build a budget tracker with variance alerts for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-011</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Reconcile invoices against POs and flag exceptions for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-012</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Clean a messy contact list: dedupe, normalize, validate for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-013</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Design a survey analysis sheet with significance flags for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-014</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a pricing calculator with tiers, discounts, and guardrails for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-015</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a churn-risk score from usage signals for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-016</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Reconcile two transaction exports and isolate mismatches for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-017</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a hiring pipeline funnel with conversion rates for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-018</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a data-entry template with validation rules for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-019</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build an inventory reorder sheet with lead-time math for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-020</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a marketing attribution sheet with UTM hygiene checks for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-021</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a commission model with caps and accelerators for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-022</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Create a loan amortization schedule with extra-payment scenarios for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-023</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a cohort retention table from raw events for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-024</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Build a capacity plan from velocity and leave data for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-025</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build a budget tracker with variance alerts for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-026</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Reconcile invoices against POs and flag exceptions for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-027</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Clean a messy contact list: dedupe, normalize, validate for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-028</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Design a survey analysis sheet with significance flags for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-029</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a pricing calculator with tiers, discounts, and guardrails for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-030</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Build a churn-risk score from usage signals for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-031</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Reconcile two transaction exports and isolate mismatches for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-032</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a hiring pipeline funnel with conversion rates for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-033</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a data-entry template with validation rules for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-034</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build an inventory reorder sheet with lead-time math for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-035</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a marketing attribution sheet with UTM hygiene checks for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-036</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a commission model with caps and accelerators for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-037</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Create a loan amortization schedule with extra-payment scenarios for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-038</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a cohort retention table from raw events for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-039</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a capacity plan from velocity and leave data for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-040</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build a budget tracker with variance alerts for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-041</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Reconcile invoices against POs and flag exceptions for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-042</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Clean a messy contact list: dedupe, normalize, validate for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-043</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Design a survey analysis sheet with significance flags for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-044</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a pricing calculator with tiers, discounts, and guardrails for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-045</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a churn-risk score from usage signals for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-046</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Reconcile two transaction exports and isolate mismatches for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-047</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a hiring pipeline funnel with conversion rates for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-048</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a data-entry template with validation rules for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-049</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build an inventory reorder sheet with lead-time math for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-050</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a marketing attribution sheet with UTM hygiene checks for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-051</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a commission model with caps and accelerators for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-052</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Create a loan amortization schedule with extra-payment scenarios for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-053</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a cohort retention table from raw events for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-054</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Build a capacity plan from velocity and leave data for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-055</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build a budget tracker with variance alerts for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-056</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Reconcile invoices against POs and flag exceptions for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-057</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Clean a messy contact list: dedupe, normalize, validate for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-058</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Design a survey analysis sheet with significance flags for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-059</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a pricing calculator with tiers, discounts, and guardrails for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-060</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Build a churn-risk score from usage signals for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-061</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Reconcile two transaction exports and isolate mismatches for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-062</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a hiring pipeline funnel with conversion rates for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-063</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a data-entry template with validation rules for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-064</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build an inventory reorder sheet with lead-time math for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-065</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a marketing attribution sheet with UTM hygiene checks for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-066</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a commission model with caps and accelerators for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-067</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Create a loan amortization schedule with extra-payment scenarios for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-068</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a cohort retention table from raw events for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-069</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a capacity plan from velocity and leave data for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-070</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build a budget tracker with variance alerts for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-071</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Reconcile invoices against POs and flag exceptions for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-072</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Clean a messy contact list: dedupe, normalize, validate for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-073</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Design a survey analysis sheet with significance flags for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-074</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a pricing calculator with tiers, discounts, and guardrails for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-075</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a churn-risk score from usage signals for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-076</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Reconcile two transaction exports and isolate mismatches for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-077</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a hiring pipeline funnel with conversion rates for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-078</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a data-entry template with validation rules for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-079</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build an inventory reorder sheet with lead-time math for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-080</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a marketing attribution sheet with UTM hygiene checks for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-081</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a commission model with caps and accelerators for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-082</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Create a loan amortization schedule with extra-payment scenarios for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-083</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a cohort retention table from raw events for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-084</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Build a capacity plan from velocity and leave data for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-085</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build a budget tracker with variance alerts for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-086</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Reconcile invoices against POs and flag exceptions for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-087</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Clean a messy contact list: dedupe, normalize, validate for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-088</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Design a survey analysis sheet with significance flags for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-089</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a pricing calculator with tiers, discounts, and guardrails for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-090</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Build a churn-risk score from usage signals for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-091</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Reconcile two transaction exports and isolate mismatches for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-092</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a hiring pipeline funnel with conversion rates for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-093</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a data-entry template with validation rules for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-094</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build an inventory reorder sheet with lead-time math for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-095</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a marketing attribution sheet with UTM hygiene checks for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-096</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a commission model with caps and accelerators for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-097</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Create a loan amortization schedule with extra-payment scenarios for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-098</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a cohort retention table from raw events for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-099</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a capacity plan from velocity and leave data for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-100</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build a budget tracker with variance alerts for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-101</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Reconcile invoices against POs and flag exceptions for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-102</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Clean a messy contact list: dedupe, normalize, validate for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-103</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Design a survey analysis sheet with significance flags for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-104</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a pricing calculator with tiers, discounts, and guardrails for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-105</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a churn-risk score from usage signals for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-106</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Reconcile two transaction exports and isolate mismatches for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-107</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a hiring pipeline funnel with conversion rates for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-108</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a data-entry template with validation rules for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-109</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build an inventory reorder sheet with lead-time math for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-110</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a marketing attribution sheet with UTM hygiene checks for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-111</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a commission model with caps and accelerators for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-112</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Create a loan amortization schedule with extra-payment scenarios for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-113</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a cohort retention table from raw events for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-114</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Build a capacity plan from velocity and leave data for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-115</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build a budget tracker with variance alerts for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-116</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Reconcile invoices against POs and flag exceptions for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-117</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Clean a messy contact list: dedupe, normalize, validate for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-118</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Design a survey analysis sheet with significance flags for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-119</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a pricing calculator with tiers, discounts, and guardrails for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-120</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Build a churn-risk score from usage signals for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-121</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Reconcile two transaction exports and isolate mismatches for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-122</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a hiring pipeline funnel with conversion rates for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-123</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a data-entry template with validation rules for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-124</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build an inventory reorder sheet with lead-time math for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-125</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a marketing attribution sheet with UTM hygiene checks for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-126</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a commission model with caps and accelerators for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-127</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Create a loan amortization schedule with extra-payment scenarios for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-128</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a cohort retention table from raw events for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-129</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a capacity plan from velocity and leave data for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-130</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build a budget tracker with variance alerts for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-131</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Reconcile invoices against POs and flag exceptions for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-132</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Clean a messy contact list: dedupe, normalize, validate for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-133</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Design a survey analysis sheet with significance flags for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-134</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a pricing calculator with tiers, discounts, and guardrails for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-135</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a churn-risk score from usage signals for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-136</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Reconcile two transaction exports and isolate mismatches for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-137</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a hiring pipeline funnel with conversion rates for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-138</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a data-entry template with validation rules for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-139</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build an inventory reorder sheet with lead-time math for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-140</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a marketing attribution sheet with UTM hygiene checks for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-141</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a commission model with caps and accelerators for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-142</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Create a loan amortization schedule with extra-payment scenarios for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-143</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a cohort retention table from raw events for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-144</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Build a capacity plan from velocity and leave data for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-145</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build a budget tracker with variance alerts for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-146</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Reconcile invoices against POs and flag exceptions for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-147</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Clean a messy contact list: dedupe, normalize, validate for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-148</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Design a survey analysis sheet with significance flags for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-149</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a pricing calculator with tiers, discounts, and guardrails for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-150</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Build a churn-risk score from usage signals for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-151</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Reconcile two transaction exports and isolate mismatches for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-152</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a hiring pipeline funnel with conversion rates for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-153</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a data-entry template with validation rules for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-154</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build an inventory reorder sheet with lead-time math for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-155</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a marketing attribution sheet with UTM hygiene checks for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-156</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a commission model with caps and accelerators for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-157</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Create a loan amortization schedule with extra-payment scenarios for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-158</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a cohort retention table from raw events for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-159</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a capacity plan from velocity and leave data for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-160</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build a budget tracker with variance alerts for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-161</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Reconcile invoices against POs and flag exceptions for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-162</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Clean a messy contact list: dedupe, normalize, validate for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-163</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Design a survey analysis sheet with significance flags for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-164</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a pricing calculator with tiers, discounts, and guardrails for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-165</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a churn-risk score from usage signals for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-166</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Reconcile two transaction exports and isolate mismatches for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-167</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a hiring pipeline funnel with conversion rates for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-168</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a data-entry template with validation rules for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-169</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build an inventory reorder sheet with lead-time math for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-170</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a marketing attribution sheet with UTM hygiene checks for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-171</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a commission model with caps and accelerators for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-172</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Create a loan amortization schedule with extra-payment scenarios for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-173</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a cohort retention table from raw events for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-174</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Build a capacity plan from velocity and leave data for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-175</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build a budget tracker with variance alerts for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-176</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Reconcile invoices against POs and flag exceptions for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-177</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Clean a messy contact list: dedupe, normalize, validate for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-178</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Design a survey analysis sheet with significance flags for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-179</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a pricing calculator with tiers, discounts, and guardrails for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-180</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Build a churn-risk score from usage signals for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-181</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Reconcile two transaction exports and isolate mismatches for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-182</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a hiring pipeline funnel with conversion rates for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-183</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Design a data-entry template with validation rules for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-184</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build an inventory reorder sheet with lead-time math for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-185</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Build a marketing attribution sheet with UTM hygiene checks for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-186</code> - design a commission model with caps and accelerators (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a commission model with caps and accelerators for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-187</code> - create a loan amortization schedule with extra-payment scenarios (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Create a loan amortization schedule with extra-payment scenarios for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-188</code> - create a cohort retention table from raw events (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Create a cohort retention table from raw events for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-189</code> - build a capacity plan from velocity and leave data (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a capacity plan from velocity and leave data for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-190</code> - build a budget tracker with variance alerts (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Build a budget tracker with variance alerts for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-191</code> - reconcile invoices against POs and flag exceptions (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Reconcile invoices against POs and flag exceptions for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-192</code> - clean a messy contact list: dedupe, normalize, validate (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Clean a messy contact list: dedupe, normalize, validate for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-193</code> - design a survey analysis sheet with significance flags (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Design a survey analysis sheet with significance flags for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-194</code> - build a pricing calculator with tiers, discounts, and guardrails (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a pricing calculator with tiers, discounts, and guardrails for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
<summary><code>spreadsheets-data-195</code> - build a churn-risk score from usage signals (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior FP&A analyst.
Build a churn-risk score from usage signals for a SaaS startup.
The intended result is a model with sensitivity scenarios.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Use tools where they help; state what evidence you checked before acting.
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
<summary><code>spreadsheets-data-196</code> - reconcile two transaction exports and isolate mismatches (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an operations data lead.
Reconcile two transaction exports and isolate mismatches for a marketplace seller.
The intended result is a CSV of cleaned rows plus a reject log.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
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
<summary><code>spreadsheets-data-197</code> - create a hiring pipeline funnel with conversion rates (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior RevOps analyst.
Create a hiring pipeline funnel with conversion rates for a nonprofit.
The intended result is a dashboard-ready summary with charts described.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Keep a searchable working note so the task survives context compaction.
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
<summary><code>spreadsheets-data-198</code> - design a data-entry template with validation rules (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert data-quality engineer.
Design a data-entry template with validation rules for a sales ops team.
The intended result is a reconciliation table with exception reasons.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Compare against the provided reference and fix the largest gaps first.
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
<summary><code>spreadsheets-data-199</code> - build an inventory reorder sheet with lead-time math (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as a senior data analyst.
Build an inventory reorder sheet with lead-time math for a finance team.
The intended result is a clean workbook spec plus formulas.
Requirements: preserve raw data on a separate untouched sheet; every formula must be auditable; no
hard-coded magic numbers.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
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
<summary><code>spreadsheets-data-200</code> - build a marketing attribution sheet with UTM hygiene checks (click to expand)</summary>

```text
Target model: Claude Opus 5.5 (claude-opus-5-5).
Act as an expert spreadsheet modeler.
Build a marketing attribution sheet with UTM hygiene checks for a manufacturing planner.
The intended result is a QA checklist with check totals.
Requirements: validate totals against source data before concluding; use consistent date, currency,
and timezone handling.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
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
