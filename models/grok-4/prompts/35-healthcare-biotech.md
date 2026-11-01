# 🏥 Healthcare & Biotech - 120 copyable Grok 4 prompts

> Clinical workflows, EHR, trials, and diagnostics (analysis only, not medical advice).

> Target model: Grok 4 (`grok-4`). xAI flagship; 256K context; real-time web; strong reasoning.

> Safety: defensive / authorized-scope use only. Stop before destructive, irreversible, sending, purchasing, deleting, or permission-changing steps without approval.

**Jump:** [Model index](../../README.md) · [Search all](prompts_index.json)

How to use: click any prompt title to expand it top to bottom, then use the copy icon on the code block.

<details>
<summary><code>healthcare-biotech-001</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design an EHR data-quality audit for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>healthcare-biotech-002</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a cohort study design for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>healthcare-biotech-003</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a care-gap identification report for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>healthcare-biotech-004</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a telehealth triage flow for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>healthcare-biotech-005</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a wearable-data aggregation pipeline for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>healthcare-biotech-006</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a lab-result normalization pipeline for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>healthcare-biotech-007</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a genomics variant annotation plan for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>healthcare-biotech-008</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a pharmacovigilance signal detector for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>healthcare-biotech-009</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a population-health dashboard for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>healthcare-biotech-010</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a diagnostic decision-support outline for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>healthcare-biotech-011</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a medication reconciliation tool for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>healthcare-biotech-012</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a patient-journey map from records for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>healthcare-biotech-013</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a clinical NLP extraction schema for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>healthcare-biotech-014</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a clinical-trial eligibility screener for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>healthcare-biotech-015</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a HIPAA compliance checklist for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>healthcare-biotech-016</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design an EHR data-quality audit for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>healthcare-biotech-017</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a cohort study design for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>healthcare-biotech-018</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a care-gap identification report for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>healthcare-biotech-019</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a telehealth triage flow for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>healthcare-biotech-020</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a wearable-data aggregation pipeline for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>healthcare-biotech-021</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a lab-result normalization pipeline for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>healthcare-biotech-022</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a genomics variant annotation plan for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>healthcare-biotech-023</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a pharmacovigilance signal detector for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>healthcare-biotech-024</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a population-health dashboard for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>healthcare-biotech-025</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a diagnostic decision-support outline for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>healthcare-biotech-026</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a medication reconciliation tool for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
```
</details>

<details>
<summary><code>healthcare-biotech-027</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a patient-journey map from records for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>healthcare-biotech-028</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a clinical NLP extraction schema for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
```
</details>

<details>
<summary><code>healthcare-biotech-029</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a clinical-trial eligibility screener for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>healthcare-biotech-030</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a HIPAA compliance checklist for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
```
</details>

<details>
<summary><code>healthcare-biotech-031</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design an EHR data-quality audit for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 31.
```
</details>

<details>
<summary><code>healthcare-biotech-032</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a cohort study design for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 32.
```
</details>

<details>
<summary><code>healthcare-biotech-033</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a care-gap identification report for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-034</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a telehealth triage flow for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 34.
```
</details>

<details>
<summary><code>healthcare-biotech-035</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a wearable-data aggregation pipeline for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 35.
```
</details>

<details>
<summary><code>healthcare-biotech-036</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a lab-result normalization pipeline for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 36.
```
</details>

<details>
<summary><code>healthcare-biotech-037</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a genomics variant annotation plan for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 37.
```
</details>

<details>
<summary><code>healthcare-biotech-038</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a pharmacovigilance signal detector for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 38.
```
</details>

<details>
<summary><code>healthcare-biotech-039</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a population-health dashboard for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 39.
```
</details>

<details>
<summary><code>healthcare-biotech-040</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a diagnostic decision-support outline for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-041</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a medication reconciliation tool for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 41.
```
</details>

<details>
<summary><code>healthcare-biotech-042</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a patient-journey map from records for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 42.
```
</details>

<details>
<summary><code>healthcare-biotech-043</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a clinical NLP extraction schema for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 43.
```
</details>

<details>
<summary><code>healthcare-biotech-044</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a clinical-trial eligibility screener for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 44.
```
</details>

<details>
<summary><code>healthcare-biotech-045</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a HIPAA compliance checklist for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-046</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design an EHR data-quality audit for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 46.
```
</details>

<details>
<summary><code>healthcare-biotech-047</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a cohort study design for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 47.
```
</details>

<details>
<summary><code>healthcare-biotech-048</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a care-gap identification report for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 48.
```
</details>

<details>
<summary><code>healthcare-biotech-049</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a telehealth triage flow for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 49.
```
</details>

<details>
<summary><code>healthcare-biotech-050</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a wearable-data aggregation pipeline for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 50.
```
</details>

<details>
<summary><code>healthcare-biotech-051</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a lab-result normalization pipeline for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 51.
```
</details>

<details>
<summary><code>healthcare-biotech-052</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a genomics variant annotation plan for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 52.
```
</details>

<details>
<summary><code>healthcare-biotech-053</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a pharmacovigilance signal detector for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 53.
```
</details>

<details>
<summary><code>healthcare-biotech-054</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a population-health dashboard for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 54.
```
</details>

<details>
<summary><code>healthcare-biotech-055</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a diagnostic decision-support outline for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 55.
```
</details>

<details>
<summary><code>healthcare-biotech-056</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a medication reconciliation tool for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 56.
```
</details>

<details>
<summary><code>healthcare-biotech-057</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a patient-journey map from records for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 57.
```
</details>

<details>
<summary><code>healthcare-biotech-058</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a clinical NLP extraction schema for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-059</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a clinical-trial eligibility screener for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 59.
```
</details>

<details>
<summary><code>healthcare-biotech-060</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a HIPAA compliance checklist for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 60.
```
</details>

<details>
<summary><code>healthcare-biotech-061</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design an EHR data-quality audit for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 61.
```
</details>

<details>
<summary><code>healthcare-biotech-062</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a cohort study design for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 62.
```
</details>

<details>
<summary><code>healthcare-biotech-063</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a care-gap identification report for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-064</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a telehealth triage flow for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 64.
```
</details>

<details>
<summary><code>healthcare-biotech-065</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a wearable-data aggregation pipeline for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 65.
```
</details>

<details>
<summary><code>healthcare-biotech-066</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a lab-result normalization pipeline for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 66.
```
</details>

<details>
<summary><code>healthcare-biotech-067</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a genomics variant annotation plan for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 67.
```
</details>

<details>
<summary><code>healthcare-biotech-068</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a pharmacovigilance signal detector for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 68.
```
</details>

<details>
<summary><code>healthcare-biotech-069</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a population-health dashboard for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 69.
```
</details>

<details>
<summary><code>healthcare-biotech-070</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a diagnostic decision-support outline for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-071</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a medication reconciliation tool for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 71.
```
</details>

<details>
<summary><code>healthcare-biotech-072</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a patient-journey map from records for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 72.
```
</details>

<details>
<summary><code>healthcare-biotech-073</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a clinical NLP extraction schema for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 73.
```
</details>

<details>
<summary><code>healthcare-biotech-074</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a clinical-trial eligibility screener for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 74.
```
</details>

<details>
<summary><code>healthcare-biotech-075</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a HIPAA compliance checklist for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-076</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design an EHR data-quality audit for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 76.
```
</details>

<details>
<summary><code>healthcare-biotech-077</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a cohort study design for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 77.
```
</details>

<details>
<summary><code>healthcare-biotech-078</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a care-gap identification report for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 78.
```
</details>

<details>
<summary><code>healthcare-biotech-079</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a telehealth triage flow for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 79.
```
</details>

<details>
<summary><code>healthcare-biotech-080</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a wearable-data aggregation pipeline for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 80.
```
</details>

<details>
<summary><code>healthcare-biotech-081</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a lab-result normalization pipeline for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 81.
```
</details>

<details>
<summary><code>healthcare-biotech-082</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a genomics variant annotation plan for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 82.
```
</details>

<details>
<summary><code>healthcare-biotech-083</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a pharmacovigilance signal detector for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 83.
```
</details>

<details>
<summary><code>healthcare-biotech-084</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a population-health dashboard for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 84.
```
</details>

<details>
<summary><code>healthcare-biotech-085</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a diagnostic decision-support outline for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 85.
```
</details>

<details>
<summary><code>healthcare-biotech-086</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a medication reconciliation tool for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 86.
```
</details>

<details>
<summary><code>healthcare-biotech-087</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a patient-journey map from records for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 87.
```
</details>

<details>
<summary><code>healthcare-biotech-088</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a clinical NLP extraction schema for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-089</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a clinical-trial eligibility screener for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 89.
```
</details>

<details>
<summary><code>healthcare-biotech-090</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a HIPAA compliance checklist for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 90.
```
</details>

<details>
<summary><code>healthcare-biotech-091</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design an EHR data-quality audit for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 91.
```
</details>

<details>
<summary><code>healthcare-biotech-092</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a cohort study design for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 92.
```
</details>

<details>
<summary><code>healthcare-biotech-093</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a care-gap identification report for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-094</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a telehealth triage flow for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 94.
```
</details>

<details>
<summary><code>healthcare-biotech-095</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a wearable-data aggregation pipeline for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 95.
```
</details>

<details>
<summary><code>healthcare-biotech-096</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a lab-result normalization pipeline for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 96.
```
</details>

<details>
<summary><code>healthcare-biotech-097</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a genomics variant annotation plan for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 97.
```
</details>

<details>
<summary><code>healthcare-biotech-098</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a pharmacovigilance signal detector for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 98.
```
</details>

<details>
<summary><code>healthcare-biotech-099</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a population-health dashboard for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 99.
```
</details>

<details>
<summary><code>healthcare-biotech-100</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a diagnostic decision-support outline for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-101</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a medication reconciliation tool for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 101.
```
</details>

<details>
<summary><code>healthcare-biotech-102</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a patient-journey map from records for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 102.
```
</details>

<details>
<summary><code>healthcare-biotech-103</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a clinical NLP extraction schema for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 103.
```
</details>

<details>
<summary><code>healthcare-biotech-104</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a clinical-trial eligibility screener for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 104.
```
</details>

<details>
<summary><code>healthcare-biotech-105</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a HIPAA compliance checklist for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-106</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design an EHR data-quality audit for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 106.
```
</details>

<details>
<summary><code>healthcare-biotech-107</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a cohort study design for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 107.
```
</details>

<details>
<summary><code>healthcare-biotech-108</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a care-gap identification report for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 108.
```
</details>

<details>
<summary><code>healthcare-biotech-109</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a telehealth triage flow for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 109.
```
</details>

<details>
<summary><code>healthcare-biotech-110</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a wearable-data aggregation pipeline for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 110.
```
</details>

<details>
<summary><code>healthcare-biotech-111</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a lab-result normalization pipeline for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 111.
```
</details>

<details>
<summary><code>healthcare-biotech-112</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a genomics variant annotation plan for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 112.
```
</details>

<details>
<summary><code>healthcare-biotech-113</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a pharmacovigilance signal detector for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 113.
```
</details>

<details>
<summary><code>healthcare-biotech-114</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a population-health dashboard for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 114.
```
</details>

<details>
<summary><code>healthcare-biotech-115</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a diagnostic decision-support outline for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 115.
```
</details>

<details>
<summary><code>healthcare-biotech-116</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a medication reconciliation tool for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 116.
```
</details>

<details>
<summary><code>healthcare-biotech-117</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a patient-journey map from records for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 117.
```
</details>

<details>
<summary><code>healthcare-biotech-118</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a clinical NLP extraction schema for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-119</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a clinical-trial eligibility screener for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 119.
```
</details>

<details>
<summary><code>healthcare-biotech-120</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a HIPAA compliance checklist for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 120.
```
</details>

<details>
<summary><code>healthcare-biotech-121</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design an EHR data-quality audit for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 121.
```
</details>

<details>
<summary><code>healthcare-biotech-122</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a cohort study design for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 122.
```
</details>

<details>
<summary><code>healthcare-biotech-123</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a care-gap identification report for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-124</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a telehealth triage flow for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 124.
```
</details>

<details>
<summary><code>healthcare-biotech-125</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a wearable-data aggregation pipeline for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 125.
```
</details>

<details>
<summary><code>healthcare-biotech-126</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a lab-result normalization pipeline for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 126.
```
</details>

<details>
<summary><code>healthcare-biotech-127</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a genomics variant annotation plan for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 127.
```
</details>

<details>
<summary><code>healthcare-biotech-128</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a pharmacovigilance signal detector for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 128.
```
</details>

<details>
<summary><code>healthcare-biotech-129</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a population-health dashboard for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 129.
```
</details>

<details>
<summary><code>healthcare-biotech-130</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a diagnostic decision-support outline for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-131</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a medication reconciliation tool for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 131.
```
</details>

<details>
<summary><code>healthcare-biotech-132</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a patient-journey map from records for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 132.
```
</details>

<details>
<summary><code>healthcare-biotech-133</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a clinical NLP extraction schema for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 133.
```
</details>

<details>
<summary><code>healthcare-biotech-134</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a clinical-trial eligibility screener for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 134.
```
</details>

<details>
<summary><code>healthcare-biotech-135</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a HIPAA compliance checklist for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-136</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design an EHR data-quality audit for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 136.
```
</details>

<details>
<summary><code>healthcare-biotech-137</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a cohort study design for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 137.
```
</details>

<details>
<summary><code>healthcare-biotech-138</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a care-gap identification report for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 138.
```
</details>

<details>
<summary><code>healthcare-biotech-139</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a telehealth triage flow for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 139.
```
</details>

<details>
<summary><code>healthcare-biotech-140</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a wearable-data aggregation pipeline for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 140.
```
</details>

<details>
<summary><code>healthcare-biotech-141</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a lab-result normalization pipeline for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 141.
```
</details>

<details>
<summary><code>healthcare-biotech-142</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a genomics variant annotation plan for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 142.
```
</details>

<details>
<summary><code>healthcare-biotech-143</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a pharmacovigilance signal detector for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 143.
```
</details>

<details>
<summary><code>healthcare-biotech-144</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a population-health dashboard for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 144.
```
</details>

<details>
<summary><code>healthcare-biotech-145</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a diagnostic decision-support outline for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 145.
```
</details>

<details>
<summary><code>healthcare-biotech-146</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a medication reconciliation tool for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 146.
```
</details>

<details>
<summary><code>healthcare-biotech-147</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a patient-journey map from records for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 147.
```
</details>

<details>
<summary><code>healthcare-biotech-148</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a clinical NLP extraction schema for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-149</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a clinical-trial eligibility screener for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 149.
```
</details>

<details>
<summary><code>healthcare-biotech-150</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a HIPAA compliance checklist for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 150.
```
</details>

<details>
<summary><code>healthcare-biotech-151</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design an EHR data-quality audit for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 151.
```
</details>

<details>
<summary><code>healthcare-biotech-152</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a cohort study design for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 152.
```
</details>

<details>
<summary><code>healthcare-biotech-153</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a care-gap identification report for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-154</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a telehealth triage flow for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 154.
```
</details>

<details>
<summary><code>healthcare-biotech-155</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a wearable-data aggregation pipeline for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 155.
```
</details>

<details>
<summary><code>healthcare-biotech-156</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a lab-result normalization pipeline for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 156.
```
</details>

<details>
<summary><code>healthcare-biotech-157</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a genomics variant annotation plan for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 157.
```
</details>

<details>
<summary><code>healthcare-biotech-158</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a pharmacovigilance signal detector for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 158.
```
</details>

<details>
<summary><code>healthcare-biotech-159</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a population-health dashboard for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 159.
```
</details>

<details>
<summary><code>healthcare-biotech-160</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a diagnostic decision-support outline for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-161</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a medication reconciliation tool for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 161.
```
</details>

<details>
<summary><code>healthcare-biotech-162</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a patient-journey map from records for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 162.
```
</details>

<details>
<summary><code>healthcare-biotech-163</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a clinical NLP extraction schema for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 163.
```
</details>

<details>
<summary><code>healthcare-biotech-164</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a clinical-trial eligibility screener for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 164.
```
</details>

<details>
<summary><code>healthcare-biotech-165</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a HIPAA compliance checklist for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-166</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design an EHR data-quality audit for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 166.
```
</details>

<details>
<summary><code>healthcare-biotech-167</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a cohort study design for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 167.
```
</details>

<details>
<summary><code>healthcare-biotech-168</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a care-gap identification report for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 168.
```
</details>

<details>
<summary><code>healthcare-biotech-169</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a telehealth triage flow for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 169.
```
</details>

<details>
<summary><code>healthcare-biotech-170</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a wearable-data aggregation pipeline for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 170.
```
</details>

<details>
<summary><code>healthcare-biotech-171</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a lab-result normalization pipeline for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 171.
```
</details>

<details>
<summary><code>healthcare-biotech-172</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a genomics variant annotation plan for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 172.
```
</details>

<details>
<summary><code>healthcare-biotech-173</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a pharmacovigilance signal detector for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 173.
```
</details>

<details>
<summary><code>healthcare-biotech-174</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a population-health dashboard for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 174.
```
</details>

<details>
<summary><code>healthcare-biotech-175</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a diagnostic decision-support outline for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 175.
```
</details>

<details>
<summary><code>healthcare-biotech-176</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a medication reconciliation tool for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 176.
```
</details>

<details>
<summary><code>healthcare-biotech-177</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a patient-journey map from records for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 177.
```
</details>

<details>
<summary><code>healthcare-biotech-178</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a clinical NLP extraction schema for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-179</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a clinical-trial eligibility screener for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 179.
```
</details>

<details>
<summary><code>healthcare-biotech-180</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a HIPAA compliance checklist for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 180.
```
</details>

<details>
<summary><code>healthcare-biotech-181</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design an EHR data-quality audit for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 181.
```
</details>

<details>
<summary><code>healthcare-biotech-182</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a cohort study design for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 182.
```
</details>

<details>
<summary><code>healthcare-biotech-183</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a care-gap identification report for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-184</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a telehealth triage flow for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 184.
```
</details>

<details>
<summary><code>healthcare-biotech-185</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a wearable-data aggregation pipeline for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 185.
```
</details>

<details>
<summary><code>healthcare-biotech-186</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a lab-result normalization pipeline for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 186.
```
</details>

<details>
<summary><code>healthcare-biotech-187</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a genomics variant annotation plan for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 187.
```
</details>

<details>
<summary><code>healthcare-biotech-188</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a pharmacovigilance signal detector for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 188.
```
</details>

<details>
<summary><code>healthcare-biotech-189</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a population-health dashboard for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 189.
```
</details>

<details>
<summary><code>healthcare-biotech-190</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a diagnostic decision-support outline for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-191</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a medication reconciliation tool for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 191.
```
</details>

<details>
<summary><code>healthcare-biotech-192</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a patient-journey map from records for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 192.
```
</details>

<details>
<summary><code>healthcare-biotech-193</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a clinical NLP extraction schema for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 193.
```
</details>

<details>
<summary><code>healthcare-biotech-194</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a clinical-trial eligibility screener for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 194.
```
</details>

<details>
<summary><code>healthcare-biotech-195</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a HIPAA compliance checklist for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
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
<summary><code>healthcare-biotech-196</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design an EHR data-quality audit for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 196.
```
</details>

<details>
<summary><code>healthcare-biotech-197</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a cohort study design for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 197.
```
</details>

<details>
<summary><code>healthcare-biotech-198</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a care-gap identification report for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 198.
```
</details>

<details>
<summary><code>healthcare-biotech-199</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a telehealth triage flow for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 199.
```
</details>

<details>
<summary><code>healthcare-biotech-200</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a wearable-data aggregation pipeline for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 200.
```
</details>

<details>
<summary><code>healthcare-biotech-201</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a lab-result normalization pipeline for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 201.
```
</details>

<details>
<summary><code>healthcare-biotech-202</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a genomics variant annotation plan for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 202.
```
</details>

<details>
<summary><code>healthcare-biotech-203</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a pharmacovigilance signal detector for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 203.
```
</details>

<details>
<summary><code>healthcare-biotech-204</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a population-health dashboard for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 204.
```
</details>

<details>
<summary><code>healthcare-biotech-205</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a diagnostic decision-support outline for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 205.
```
</details>

<details>
<summary><code>healthcare-biotech-206</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a medication reconciliation tool for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 206.
```
</details>

<details>
<summary><code>healthcare-biotech-207</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a patient-journey map from records for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 207.
```
</details>

<details>
<summary><code>healthcare-biotech-208</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a clinical NLP extraction schema for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 208.
```
</details>

<details>
<summary><code>healthcare-biotech-209</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a clinical-trial eligibility screener for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 209.
```
</details>

<details>
<summary><code>healthcare-biotech-210</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a HIPAA compliance checklist for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 210.
```
</details>

<details>
<summary><code>healthcare-biotech-211</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design an EHR data-quality audit for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 211.
```
</details>

<details>
<summary><code>healthcare-biotech-212</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a cohort study design for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 212.
```
</details>

<details>
<summary><code>healthcare-biotech-213</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a care-gap identification report for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 213.
```
</details>

<details>
<summary><code>healthcare-biotech-214</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a telehealth triage flow for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 214.
```
</details>

<details>
<summary><code>healthcare-biotech-215</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a wearable-data aggregation pipeline for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 215.
```
</details>

<details>
<summary><code>healthcare-biotech-216</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a lab-result normalization pipeline for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 216.
```
</details>

<details>
<summary><code>healthcare-biotech-217</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a genomics variant annotation plan for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 217.
```
</details>

<details>
<summary><code>healthcare-biotech-218</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a pharmacovigilance signal detector for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 218.
```
</details>

<details>
<summary><code>healthcare-biotech-219</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a population-health dashboard for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 219.
```
</details>

<details>
<summary><code>healthcare-biotech-220</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a diagnostic decision-support outline for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 220.
```
</details>

<details>
<summary><code>healthcare-biotech-221</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a medication reconciliation tool for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 221.
```
</details>

<details>
<summary><code>healthcare-biotech-222</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a patient-journey map from records for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 222.
```
</details>

<details>
<summary><code>healthcare-biotech-223</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a clinical NLP extraction schema for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 223.
```
</details>

<details>
<summary><code>healthcare-biotech-224</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a clinical-trial eligibility screener for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 224.
```
</details>

<details>
<summary><code>healthcare-biotech-225</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a HIPAA compliance checklist for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 225.
```
</details>

<details>
<summary><code>healthcare-biotech-226</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design an EHR data-quality audit for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 226.
```
</details>

<details>
<summary><code>healthcare-biotech-227</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a cohort study design for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 227.
```
</details>

<details>
<summary><code>healthcare-biotech-228</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a care-gap identification report for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 228.
```
</details>

<details>
<summary><code>healthcare-biotech-229</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a telehealth triage flow for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 229.
```
</details>

<details>
<summary><code>healthcare-biotech-230</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a wearable-data aggregation pipeline for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 230.
```
</details>

<details>
<summary><code>healthcare-biotech-231</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a lab-result normalization pipeline for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 231.
```
</details>

<details>
<summary><code>healthcare-biotech-232</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a genomics variant annotation plan for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 232.
```
</details>

<details>
<summary><code>healthcare-biotech-233</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a pharmacovigilance signal detector for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 233.
```
</details>

<details>
<summary><code>healthcare-biotech-234</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a population-health dashboard for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 234.
```
</details>

<details>
<summary><code>healthcare-biotech-235</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a diagnostic decision-support outline for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 235.
```
</details>

<details>
<summary><code>healthcare-biotech-236</code> - build a medication reconciliation tool (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a medication reconciliation tool for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 236.
```
</details>

<details>
<summary><code>healthcare-biotech-237</code> - create a patient-journey map from records (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a patient-journey map from records for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 237.
```
</details>

<details>
<summary><code>healthcare-biotech-238</code> - design a clinical NLP extraction schema (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a clinical NLP extraction schema for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 238.
```
</details>

<details>
<summary><code>healthcare-biotech-239</code> - build a clinical-trial eligibility screener (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a clinical-trial eligibility screener for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 239.
```
</details>

<details>
<summary><code>healthcare-biotech-240</code> - create a HIPAA compliance checklist (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a HIPAA compliance checklist for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 240.
```
</details>

<details>
<summary><code>healthcare-biotech-241</code> - design an EHR data-quality audit (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design an EHR data-quality audit for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 241.
```
</details>

<details>
<summary><code>healthcare-biotech-242</code> - build a cohort study design (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a cohort study design for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 242.
```
</details>

<details>
<summary><code>healthcare-biotech-243</code> - create a care-gap identification report (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a care-gap identification report for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 243.
```
</details>

<details>
<summary><code>healthcare-biotech-244</code> - design a telehealth triage flow (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a telehealth triage flow for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 244.
```
</details>

<details>
<summary><code>healthcare-biotech-245</code> - build a wearable-data aggregation pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior health informatics lead.
Build a wearable-data aggregation pipeline for a biotech startup.
The intended result is a data pipeline.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Keep a searchable working note so the task survives context compaction.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 245.
```
</details>

<details>
<summary><code>healthcare-biotech-246</code> - create a lab-result normalization pipeline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert diagnostics aide.
Create a lab-result normalization pipeline for a clinic.
The intended result is a compliance checklist.
Requirements: require clinician review; validate on real data with ethics approval.
Compare against the provided reference and fix the largest gaps first.
xAI flagship; 256K context; real-time web; strong reasoning.
If a minor detail is unspecified, make the best professional decision and continue; ask only when
the answer would materially change the outcome.
Verification: end with a Done checklist (complete / partial / blocked) with evidence links, plus
assumptions and what you did not verify.
Variant focus 246.
```
</details>

<details>
<summary><code>healthcare-biotech-247</code> - design a genomics variant annotation plan (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior clinical data analyst.
Design a genomics variant annotation plan for a hospital.
The intended result is an analysis spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Be concrete and end-to-end: produce the artifact, not a plan to produce it.
xAI flagship; 256K context; real-time web; strong reasoning.
Bias toward action: treat 'can you / help me / I want to' as instructions to act.
Prepare a concrete reviewable result before asking for approval.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 247.
```
</details>

<details>
<summary><code>healthcare-biotech-248</code> - build a pharmacovigilance signal detector (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert biotech researcher.
Build a pharmacovigilance signal detector for a classroom.
The intended result is a review report.
Requirements: require clinician review; validate on real data with ethics approval.
Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the
brief.
xAI flagship; 256K context; real-time web; strong reasoning.
Work persistently until the goal is complete.
Use read-only exploration freely; stop before any destructive, irreversible, sending, purchasing,
deleting, or permission-changing step.
Verification: test every important interaction, list what passed/failed/unverified, fix high-impact
issues, then re-test.
Variant focus 248.
```
</details>

<details>
<summary><code>healthcare-biotech-249</code> - create a population-health dashboard (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as a senior EHR engineer.
Create a population-health dashboard for a regulator.
The intended result is a dashboard spec.
Requirements: not medical advice; for analysis only; protect PHI; HIPAA-aware.
Use tools where they help; state what evidence you checked before acting.
xAI flagship; 256K context; real-time web; strong reasoning.
Infer intent from context and carry the task to completion.
Do not emit warnings based on hypothetical risks; report only verified findings.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 249.
```
</details>

<details>
<summary><code>healthcare-biotech-250</code> - design a diagnostic decision-support outline (click to expand)</summary>

```text
Target model: Grok 4 (grok-4).
Act as an expert trial designer.
Design a diagnostic decision-support outline for a researcher.
The intended result is a study design.
Requirements: require clinician review; validate on real data with ethics approval.
Parallelize with subagents where independent work exists; merge with a single coherent voice.
xAI flagship; 256K context; real-time web; strong reasoning.
Stay within the authorized scope described here.
If project files conflict with these instructions, these instructions take precedence; quote the
conflicting file if you must pause.
Verification: keep checks proportional to risk.
For small reversible changes, run only targeted checks; for risky changes, run the full relevant
suite.
Variant focus 250.
```
</details>
