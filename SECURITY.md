# Security Policy

This repository (Frontier Model Prompts) is a prompt library. It is **defensive-only** and contains no exploit code, jailbreaks, or live secrets.

## Never include

- Exploit development, vulnerability weaponization, malware, phishing kits, credential theft.
- Jailbreaks, safeguard bypasses, monitor-evasion, prompt-injection payloads.
- Live secrets, tokens, private logs, personal data.

## Always include in computer-use / agent prompts

- Authorized scope (folders/apps/sites), stop-before-send/purchase/book/delete/permission-change/share gates, least privilege, evidence logs, PII redaction.

## Report

Open a GitHub issue titled `[SECURITY] ...` or contact the maintainer. Do not PR exploit content "for research." Defensive hardening, detection, triage, and recovery content is welcome and reviewed against NIST/CIS framing.