from pathlib import Path
p = Path("scripts/generate_model_prompts.py")
lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
target = None
for i, l in enumerate(lines):
    if "Coding agents, 3D generation" in l:
        for j in range(i+1, len(lines)):
            if lines[j].strip() == "]":
                target = j
                break
        break
assert target is not None
new = '''    dict(slug="deepseek-v3-2", display="DeepSeek V3.2", model_id="deepseek-v3.2",
         levels=["off", "low", "medium", "high", "max"], level_label="Suggested reasoning mode",
         control="Open-weight MoE; 128K context; strong coding/math. Cost-efficient frontier quality.",
         strengths="Coding, math, open weights, cost-efficient."),
    dict(slug="grok-4", display="Grok 4", model_id="grok-4",
         levels=["low", "medium", "high", "xhigh", "max"], level_label="Suggested reasoning effort",
         control="xAI flagship; 256K context; real-time web; strong reasoning.",
         strengths="Real-time web, reasoning, multimodal."),
'''
lines.insert(target, new)
p.write_text("".join(lines), encoding="utf-8")
print("done")
"