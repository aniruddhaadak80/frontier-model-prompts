# 📊 Advanced Model Testing & Evaluation - 120 copyable DeepSeek V3.2 prompts

> Evals, red-teaming, benchmarking, regression, and capability probing for frontier models.

> Target model: DeepSeek V3.2 (`deepseek-v3.2`). Open-weight MoE; 128K context; strong coding/math. Cost-efficient frontier quality.

> Safety: defensive / authorized-scope use only. Stop before destructive, irreversible, sending, purchasing, deleting, or permission-changing steps without approval.

**Jump:** [Model index](../../README.md) · [Search all](prompts_index.json)

How to use: click any prompt title to expand it top to bottom, then use the copy icon on the code block.

<details>
<summary><code>model-eval-001</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an eval suite for a coding agent with hidden tests for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>model-eval-002</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a safety refusal eval with benign and adversarial cases for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>model-eval-003</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression dashboard spec with trend alerts for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>model-eval-004</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a latency/cost/quality trade-off benchmark for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>model-eval-005</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a robustness eval with paraphrase and noise for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>model-eval-006</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a hallucination-detection eval with gold answers for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>model-eval-007</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a bias and fairness probe across demographics for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>model-eval-008</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a capability probe for tool-use reliability for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>model-eval-009</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create an agentic-task completion eval with checkpoints for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>model-eval-010</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an A/B comparison protocol for two model versions for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>model-eval-011</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a structured-output validity eval with schema checks for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>model-eval-012</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression pack that pins behavior per task type for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>model-eval-013</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a multi-turn coherence eval with state tracking for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>model-eval-014</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a red-team prompt set for jailbreak resistance for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>model-eval-015</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a long-context retrieval eval with needle tasks for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>model-eval-016</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an eval suite for a coding agent with hidden tests for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>model-eval-017</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a safety refusal eval with benign and adversarial cases for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>model-eval-018</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression dashboard spec with trend alerts for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>model-eval-019</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a latency/cost/quality trade-off benchmark for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>model-eval-020</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a robustness eval with paraphrase and noise for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>model-eval-021</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a hallucination-detection eval with gold answers for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>model-eval-022</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a bias and fairness probe across demographics for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>model-eval-023</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a capability probe for tool-use reliability for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>model-eval-024</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create an agentic-task completion eval with checkpoints for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>model-eval-025</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an A/B comparison protocol for two model versions for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>model-eval-026</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a structured-output validity eval with schema checks for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>model-eval-027</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression pack that pins behavior per task type for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>model-eval-028</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a multi-turn coherence eval with state tracking for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>model-eval-029</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a red-team prompt set for jailbreak resistance for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>model-eval-030</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a long-context retrieval eval with needle tasks for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>model-eval-031</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an eval suite for a coding agent with hidden tests for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 31.
```
</details>

<details>
<summary><code>model-eval-032</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a safety refusal eval with benign and adversarial cases for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 32.
```
</details>

<details>
<summary><code>model-eval-033</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression dashboard spec with trend alerts for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-034</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a latency/cost/quality trade-off benchmark for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 34.
```
</details>

<details>
<summary><code>model-eval-035</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a robustness eval with paraphrase and noise for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 35.
```
</details>

<details>
<summary><code>model-eval-036</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a hallucination-detection eval with gold answers for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 36.
```
</details>

<details>
<summary><code>model-eval-037</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a bias and fairness probe across demographics for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 37.
```
</details>

<details>
<summary><code>model-eval-038</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a capability probe for tool-use reliability for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 38.
```
</details>

<details>
<summary><code>model-eval-039</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create an agentic-task completion eval with checkpoints for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 39.
```
</details>

<details>
<summary><code>model-eval-040</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an A/B comparison protocol for two model versions for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-041</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a structured-output validity eval with schema checks for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 41.
```
</details>

<details>
<summary><code>model-eval-042</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression pack that pins behavior per task type for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 42.
```
</details>

<details>
<summary><code>model-eval-043</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a multi-turn coherence eval with state tracking for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 43.
```
</details>

<details>
<summary><code>model-eval-044</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a red-team prompt set for jailbreak resistance for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 44.
```
</details>

<details>
<summary><code>model-eval-045</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a long-context retrieval eval with needle tasks for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-046</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an eval suite for a coding agent with hidden tests for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 46.
```
</details>

<details>
<summary><code>model-eval-047</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a safety refusal eval with benign and adversarial cases for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 47.
```
</details>

<details>
<summary><code>model-eval-048</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression dashboard spec with trend alerts for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 48.
```
</details>

<details>
<summary><code>model-eval-049</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a latency/cost/quality trade-off benchmark for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 49.
```
</details>

<details>
<summary><code>model-eval-050</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a robustness eval with paraphrase and noise for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 50.
```
</details>

<details>
<summary><code>model-eval-051</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a hallucination-detection eval with gold answers for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 51.
```
</details>

<details>
<summary><code>model-eval-052</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a bias and fairness probe across demographics for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 52.
```
</details>

<details>
<summary><code>model-eval-053</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a capability probe for tool-use reliability for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 53.
```
</details>

<details>
<summary><code>model-eval-054</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create an agentic-task completion eval with checkpoints for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 54.
```
</details>

<details>
<summary><code>model-eval-055</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an A/B comparison protocol for two model versions for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 55.
```
</details>

<details>
<summary><code>model-eval-056</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a structured-output validity eval with schema checks for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 56.
```
</details>

<details>
<summary><code>model-eval-057</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression pack that pins behavior per task type for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 57.
```
</details>

<details>
<summary><code>model-eval-058</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a multi-turn coherence eval with state tracking for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-059</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a red-team prompt set for jailbreak resistance for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 59.
```
</details>

<details>
<summary><code>model-eval-060</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a long-context retrieval eval with needle tasks for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 60.
```
</details>

<details>
<summary><code>model-eval-061</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an eval suite for a coding agent with hidden tests for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 61.
```
</details>

<details>
<summary><code>model-eval-062</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a safety refusal eval with benign and adversarial cases for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 62.
```
</details>

<details>
<summary><code>model-eval-063</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression dashboard spec with trend alerts for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-064</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a latency/cost/quality trade-off benchmark for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 64.
```
</details>

<details>
<summary><code>model-eval-065</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a robustness eval with paraphrase and noise for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 65.
```
</details>

<details>
<summary><code>model-eval-066</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a hallucination-detection eval with gold answers for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 66.
```
</details>

<details>
<summary><code>model-eval-067</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a bias and fairness probe across demographics for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 67.
```
</details>

<details>
<summary><code>model-eval-068</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a capability probe for tool-use reliability for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 68.
```
</details>

<details>
<summary><code>model-eval-069</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create an agentic-task completion eval with checkpoints for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 69.
```
</details>

<details>
<summary><code>model-eval-070</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an A/B comparison protocol for two model versions for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-071</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a structured-output validity eval with schema checks for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 71.
```
</details>

<details>
<summary><code>model-eval-072</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression pack that pins behavior per task type for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 72.
```
</details>

<details>
<summary><code>model-eval-073</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a multi-turn coherence eval with state tracking for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 73.
```
</details>

<details>
<summary><code>model-eval-074</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a red-team prompt set for jailbreak resistance for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 74.
```
</details>

<details>
<summary><code>model-eval-075</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a long-context retrieval eval with needle tasks for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-076</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an eval suite for a coding agent with hidden tests for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 76.
```
</details>

<details>
<summary><code>model-eval-077</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a safety refusal eval with benign and adversarial cases for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 77.
```
</details>

<details>
<summary><code>model-eval-078</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression dashboard spec with trend alerts for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 78.
```
</details>

<details>
<summary><code>model-eval-079</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a latency/cost/quality trade-off benchmark for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 79.
```
</details>

<details>
<summary><code>model-eval-080</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a robustness eval with paraphrase and noise for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 80.
```
</details>

<details>
<summary><code>model-eval-081</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a hallucination-detection eval with gold answers for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 81.
```
</details>

<details>
<summary><code>model-eval-082</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a bias and fairness probe across demographics for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 82.
```
</details>

<details>
<summary><code>model-eval-083</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a capability probe for tool-use reliability for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 83.
```
</details>

<details>
<summary><code>model-eval-084</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create an agentic-task completion eval with checkpoints for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 84.
```
</details>

<details>
<summary><code>model-eval-085</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an A/B comparison protocol for two model versions for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 85.
```
</details>

<details>
<summary><code>model-eval-086</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a structured-output validity eval with schema checks for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 86.
```
</details>

<details>
<summary><code>model-eval-087</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression pack that pins behavior per task type for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 87.
```
</details>

<details>
<summary><code>model-eval-088</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a multi-turn coherence eval with state tracking for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-089</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a red-team prompt set for jailbreak resistance for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 89.
```
</details>

<details>
<summary><code>model-eval-090</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a long-context retrieval eval with needle tasks for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 90.
```
</details>

<details>
<summary><code>model-eval-091</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an eval suite for a coding agent with hidden tests for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 91.
```
</details>

<details>
<summary><code>model-eval-092</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a safety refusal eval with benign and adversarial cases for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 92.
```
</details>

<details>
<summary><code>model-eval-093</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression dashboard spec with trend alerts for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-094</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a latency/cost/quality trade-off benchmark for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 94.
```
</details>

<details>
<summary><code>model-eval-095</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a robustness eval with paraphrase and noise for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 95.
```
</details>

<details>
<summary><code>model-eval-096</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a hallucination-detection eval with gold answers for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 96.
```
</details>

<details>
<summary><code>model-eval-097</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a bias and fairness probe across demographics for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 97.
```
</details>

<details>
<summary><code>model-eval-098</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a capability probe for tool-use reliability for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 98.
```
</details>

<details>
<summary><code>model-eval-099</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create an agentic-task completion eval with checkpoints for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 99.
```
</details>

<details>
<summary><code>model-eval-100</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an A/B comparison protocol for two model versions for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-101</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a structured-output validity eval with schema checks for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 101.
```
</details>

<details>
<summary><code>model-eval-102</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression pack that pins behavior per task type for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 102.
```
</details>

<details>
<summary><code>model-eval-103</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a multi-turn coherence eval with state tracking for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 103.
```
</details>

<details>
<summary><code>model-eval-104</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a red-team prompt set for jailbreak resistance for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 104.
```
</details>

<details>
<summary><code>model-eval-105</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a long-context retrieval eval with needle tasks for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-106</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an eval suite for a coding agent with hidden tests for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 106.
```
</details>

<details>
<summary><code>model-eval-107</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a safety refusal eval with benign and adversarial cases for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 107.
```
</details>

<details>
<summary><code>model-eval-108</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression dashboard spec with trend alerts for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 108.
```
</details>

<details>
<summary><code>model-eval-109</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a latency/cost/quality trade-off benchmark for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 109.
```
</details>

<details>
<summary><code>model-eval-110</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a robustness eval with paraphrase and noise for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 110.
```
</details>

<details>
<summary><code>model-eval-111</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a hallucination-detection eval with gold answers for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 111.
```
</details>

<details>
<summary><code>model-eval-112</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a bias and fairness probe across demographics for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 112.
```
</details>

<details>
<summary><code>model-eval-113</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a capability probe for tool-use reliability for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 113.
```
</details>

<details>
<summary><code>model-eval-114</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create an agentic-task completion eval with checkpoints for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 114.
```
</details>

<details>
<summary><code>model-eval-115</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an A/B comparison protocol for two model versions for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 115.
```
</details>

<details>
<summary><code>model-eval-116</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a structured-output validity eval with schema checks for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 116.
```
</details>

<details>
<summary><code>model-eval-117</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression pack that pins behavior per task type for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 117.
```
</details>

<details>
<summary><code>model-eval-118</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a multi-turn coherence eval with state tracking for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-119</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a red-team prompt set for jailbreak resistance for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 119.
```
</details>

<details>
<summary><code>model-eval-120</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a long-context retrieval eval with needle tasks for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 120.
```
</details>

<details>
<summary><code>model-eval-121</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an eval suite for a coding agent with hidden tests for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 121.
```
</details>

<details>
<summary><code>model-eval-122</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a safety refusal eval with benign and adversarial cases for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 122.
```
</details>

<details>
<summary><code>model-eval-123</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression dashboard spec with trend alerts for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-124</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a latency/cost/quality trade-off benchmark for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 124.
```
</details>

<details>
<summary><code>model-eval-125</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a robustness eval with paraphrase and noise for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 125.
```
</details>

<details>
<summary><code>model-eval-126</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a hallucination-detection eval with gold answers for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 126.
```
</details>

<details>
<summary><code>model-eval-127</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a bias and fairness probe across demographics for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 127.
```
</details>

<details>
<summary><code>model-eval-128</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a capability probe for tool-use reliability for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 128.
```
</details>

<details>
<summary><code>model-eval-129</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create an agentic-task completion eval with checkpoints for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 129.
```
</details>

<details>
<summary><code>model-eval-130</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an A/B comparison protocol for two model versions for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-131</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a structured-output validity eval with schema checks for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 131.
```
</details>

<details>
<summary><code>model-eval-132</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression pack that pins behavior per task type for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 132.
```
</details>

<details>
<summary><code>model-eval-133</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a multi-turn coherence eval with state tracking for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 133.
```
</details>

<details>
<summary><code>model-eval-134</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a red-team prompt set for jailbreak resistance for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 134.
```
</details>

<details>
<summary><code>model-eval-135</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a long-context retrieval eval with needle tasks for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-136</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an eval suite for a coding agent with hidden tests for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 136.
```
</details>

<details>
<summary><code>model-eval-137</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a safety refusal eval with benign and adversarial cases for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 137.
```
</details>

<details>
<summary><code>model-eval-138</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression dashboard spec with trend alerts for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 138.
```
</details>

<details>
<summary><code>model-eval-139</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a latency/cost/quality trade-off benchmark for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 139.
```
</details>

<details>
<summary><code>model-eval-140</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a robustness eval with paraphrase and noise for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 140.
```
</details>

<details>
<summary><code>model-eval-141</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a hallucination-detection eval with gold answers for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 141.
```
</details>

<details>
<summary><code>model-eval-142</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a bias and fairness probe across demographics for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 142.
```
</details>

<details>
<summary><code>model-eval-143</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a capability probe for tool-use reliability for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 143.
```
</details>

<details>
<summary><code>model-eval-144</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create an agentic-task completion eval with checkpoints for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 144.
```
</details>

<details>
<summary><code>model-eval-145</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an A/B comparison protocol for two model versions for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 145.
```
</details>

<details>
<summary><code>model-eval-146</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a structured-output validity eval with schema checks for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 146.
```
</details>

<details>
<summary><code>model-eval-147</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression pack that pins behavior per task type for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 147.
```
</details>

<details>
<summary><code>model-eval-148</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a multi-turn coherence eval with state tracking for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-149</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a red-team prompt set for jailbreak resistance for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 149.
```
</details>

<details>
<summary><code>model-eval-150</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a long-context retrieval eval with needle tasks for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 150.
```
</details>

<details>
<summary><code>model-eval-151</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an eval suite for a coding agent with hidden tests for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 151.
```
</details>

<details>
<summary><code>model-eval-152</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a safety refusal eval with benign and adversarial cases for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 152.
```
</details>

<details>
<summary><code>model-eval-153</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression dashboard spec with trend alerts for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-154</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a latency/cost/quality trade-off benchmark for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 154.
```
</details>

<details>
<summary><code>model-eval-155</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a robustness eval with paraphrase and noise for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 155.
```
</details>

<details>
<summary><code>model-eval-156</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a hallucination-detection eval with gold answers for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 156.
```
</details>

<details>
<summary><code>model-eval-157</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a bias and fairness probe across demographics for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 157.
```
</details>

<details>
<summary><code>model-eval-158</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a capability probe for tool-use reliability for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 158.
```
</details>

<details>
<summary><code>model-eval-159</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create an agentic-task completion eval with checkpoints for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 159.
```
</details>

<details>
<summary><code>model-eval-160</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an A/B comparison protocol for two model versions for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-161</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a structured-output validity eval with schema checks for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 161.
```
</details>

<details>
<summary><code>model-eval-162</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression pack that pins behavior per task type for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 162.
```
</details>

<details>
<summary><code>model-eval-163</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a multi-turn coherence eval with state tracking for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 163.
```
</details>

<details>
<summary><code>model-eval-164</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a red-team prompt set for jailbreak resistance for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 164.
```
</details>

<details>
<summary><code>model-eval-165</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a long-context retrieval eval with needle tasks for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-166</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an eval suite for a coding agent with hidden tests for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 166.
```
</details>

<details>
<summary><code>model-eval-167</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a safety refusal eval with benign and adversarial cases for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 167.
```
</details>

<details>
<summary><code>model-eval-168</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression dashboard spec with trend alerts for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 168.
```
</details>

<details>
<summary><code>model-eval-169</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a latency/cost/quality trade-off benchmark for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 169.
```
</details>

<details>
<summary><code>model-eval-170</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a robustness eval with paraphrase and noise for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 170.
```
</details>

<details>
<summary><code>model-eval-171</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a hallucination-detection eval with gold answers for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 171.
```
</details>

<details>
<summary><code>model-eval-172</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a bias and fairness probe across demographics for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 172.
```
</details>

<details>
<summary><code>model-eval-173</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a capability probe for tool-use reliability for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 173.
```
</details>

<details>
<summary><code>model-eval-174</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create an agentic-task completion eval with checkpoints for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 174.
```
</details>

<details>
<summary><code>model-eval-175</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an A/B comparison protocol for two model versions for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 175.
```
</details>

<details>
<summary><code>model-eval-176</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a structured-output validity eval with schema checks for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 176.
```
</details>

<details>
<summary><code>model-eval-177</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression pack that pins behavior per task type for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 177.
```
</details>

<details>
<summary><code>model-eval-178</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a multi-turn coherence eval with state tracking for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-179</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a red-team prompt set for jailbreak resistance for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 179.
```
</details>

<details>
<summary><code>model-eval-180</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a long-context retrieval eval with needle tasks for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 180.
```
</details>

<details>
<summary><code>model-eval-181</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design an eval suite for a coding agent with hidden tests for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 181.
```
</details>

<details>
<summary><code>model-eval-182</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a safety refusal eval with benign and adversarial cases for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 182.
```
</details>

<details>
<summary><code>model-eval-183</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a regression dashboard spec with trend alerts for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-184</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design a latency/cost/quality trade-off benchmark for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 184.
```
</details>

<details>
<summary><code>model-eval-185</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a robustness eval with paraphrase and noise for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 185.
```
</details>

<details>
<summary><code>model-eval-186</code> - create a hallucination-detection eval with gold answers (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a hallucination-detection eval with gold answers for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 186.
```
</details>

<details>
<summary><code>model-eval-187</code> - design a bias and fairness probe across demographics (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a bias and fairness probe across demographics for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 187.
```
</details>

<details>
<summary><code>model-eval-188</code> - build a capability probe for tool-use reliability (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a capability probe for tool-use reliability for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 188.
```
</details>

<details>
<summary><code>model-eval-189</code> - create an agentic-task completion eval with checkpoints (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create an agentic-task completion eval with checkpoints for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 189.
```
</details>

<details>
<summary><code>model-eval-190</code> - design an A/B comparison protocol for two model versions (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an A/B comparison protocol for two model versions for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-191</code> - build a structured-output validity eval with schema checks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a structured-output validity eval with schema checks for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 191.
```
</details>

<details>
<summary><code>model-eval-192</code> - create a regression pack that pins behavior per task type (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression pack that pins behavior per task type for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 192.
```
</details>

<details>
<summary><code>model-eval-193</code> - design a multi-turn coherence eval with state tracking (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a multi-turn coherence eval with state tracking for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 193.
```
</details>

<details>
<summary><code>model-eval-194</code> - build a red-team prompt set for jailbreak resistance (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a red-team prompt set for jailbreak resistance for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 194.
```
</details>

<details>
<summary><code>model-eval-195</code> - create a long-context retrieval eval with needle tasks (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior benchmark designer.
Create a long-context retrieval eval with needle tasks for a classroom.
The intended result is a benchmark spec.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Use tools where they help; state what evidence you checked before acting.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
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
<summary><code>model-eval-196</code> - design an eval suite for a coding agent with hidden tests (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a ML quality engineer.
Design an eval suite for a coding agent with hidden tests for a research lab.
The intended result is a regression pack.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 196.
```
</details>

<details>
<summary><code>model-eval-197</code> - build a safety refusal eval with benign and adversarial cases (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior safety tester.
Build a safety refusal eval with benign and adversarial cases for a startup.
The intended result is a red-team report outline.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Keep a searchable working note so the task survives context compaction.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 197.
```
</details>

<details>
<summary><code>model-eval-198</code> - create a regression dashboard spec with trend alerts (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert capability analyst.
Create a regression dashboard spec with trend alerts for an enterprise pilot.
The intended result is a test matrix with oracles.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Compare against the provided reference and fix the largest gaps first.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 198.
```
</details>

<details>
<summary><code>model-eval-199</code> - design a latency/cost/quality trade-off benchmark (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as a senior eval engineer.
Design a latency/cost/quality trade-off benchmark for a model vendor.
The intended result is an eval plan with pass criteria.
Requirements: one variable per A/B; record seeds and versions; separate tested/failed/unverified in
reports.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 199.
```
</details>

<details>
<summary><code>model-eval-200</code> - build a robustness eval with paraphrase and noise (click to expand)</summary>

```text
Target model: DeepSeek V3.2 (deepseek-v3.2).
Act as an expert red-team lead.
Build a robustness eval with paraphrase and noise for open source.
The intended result is a dashboard wireframe.
Requirements: include confidence intervals where possible; redact PII; protect test data.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
Open-weight MoE; 128K context; strong coding/math.
Cost-efficient frontier quality.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 200.
```
</details>
