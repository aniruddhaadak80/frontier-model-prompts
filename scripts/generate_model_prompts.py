"""Generate prompt packs for additional frontier models.

Each pack mirrors the GPT-6 Astra structure: 28 categories x 120 prompts,
with machine-readable twins (jsonl/csv/index) and collapsible markdown blocks.
Run: py scripts/generate_model_prompts.py [model-slug|all]
"""

import importlib.util, json, csv, hashlib, textwrap, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Reuse category definitions from the Astra generator.
spec = importlib.util.spec_from_file_location(
    "gen", ROOT / "scripts" / "generate_prompts.py"
)
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)
CATEGORIES = gen.CATEGORIES
AUTONOMY = gen.AUTONOMY
VERIFY = gen.VERIFY

PER_CATEGORY = 200

MODELS = [
    dict(
        slug="opus-5-5",
        display="Claude Opus 5.5",
        model_id="claude-opus-5-5",
        levels=["low", "medium", "high", "xhigh", "max"],
        level_label="Suggested reasoning effort",
        control="Adaptive thinking is always on; steer depth with the effort parameter (default medium). Context 1M, max output 128K. $4/$20 per MTok. Knowledge cutoff Jun 2026. Cache reads 5% of base input.",
        strengths="Long-running agentic coding, vision, computer use, knowledge work.",
    ),
    dict(
        slug="gemini-4-argon",
        display="Gemini 4 Argon",
        model_id="gemini-4-argon",
        levels=["low", "medium", "high", "xhigh", "max"],
        level_label="Suggested thinking level",
        control="Sparse MoE with native multimodal (text/image/audio/video). Context 1M. Knowledge cutoff Mar 2026. Strong on knowledge work, finance/legal, cybersecurity defense.",
        strengths="Deep visual perception, multimodal document analysis, finance/legal, cybersecurity defense.",
    ),
    dict(
        slug="muse-wonder",
        display="Muse Wonder",
        model_id="muse-wonder",
        levels=["quick", "balanced", "deep", "deeper", "max"],
        level_label="Suggested reasoning depth",
        control="Active memory + goal persistence for long-context conversations. Meta Model API $4/$20. Released Oct 12, 2026. Strong agentic task completion.",
        strengths="Long-context conversations, active memory, goal persistence, agentic tasks.",
    ),
    dict(
        slug="kimi-k-3-1",
        display="Kimi K 3.1 Pro",
        model_id="kimi-k-3-1-pro",
        levels=["off", "low", "medium", "high", "max"],
        level_label="Suggested thinking mode",
        control="Open-weight 3T-class MoE; 1M context; text+image. Released Oct 23, 2026. Strong coding-agent performance and 3D generation.",
        strengths="Coding agents, 3D generation, open weights, cost-efficient frontier quality.",
    ),
    dict(
        slug="deepseek-v3-2",
        display="DeepSeek V3.2",
        model_id="deepseek-v3.2",
        levels=["off", "low", "medium", "high", "max"],
        level_label="Suggested reasoning mode",
        control="Open-weight MoE; 128K context; strong coding/math. Cost-efficient frontier quality.",
        strengths="Coding, math, open weights, cost-efficient.",
    ),
    dict(
        slug="grok-4",
        display="Grok 4",
        model_id="grok-4",
        levels=["low", "medium", "high", "xhigh", "max"],
        level_label="Suggested reasoning effort",
        control="xAI flagship; 256K context; real-time web; strong reasoning.",
        strengths="Real-time web, reasoning, multimodal.",
    ),
]

EFFORT_CATS = {"coding", "reasoning", "multi-agent", "devops", "testing", "migration"}


def build_prompt(cat, i, model):
    n_roles = len(cat["roles"])
    n_tasks = len(cat["tasks"])
    n_aud = len(cat["audiences"])
    n_con = len(cat["constraints"])
    n_out = len(cat["outputs"])
    role = cat["roles"][i % n_roles]
    task = cat["tasks"][(i * 7) % n_tasks]
    aud = cat["audiences"][(i * 5) % n_aud]
    con = cat["constraints"][(i * 3) % n_con]
    con2 = cat["constraints"][(i * 3 + 1) % n_con]
    out = cat["outputs"][(i * 11) % n_out]
    autonomy = AUTONOMY[i % len(AUTONOMY)]
    verify = VERIFY[(i // 2) % len(VERIFY)]
    is_effort_cat = any(k in cat["slug"] for k in EFFORT_CATS)
    effort = model["levels"][i % len(model["levels"])] if is_effort_cat else None
    angle = [
        "Be concrete and end-to-end: produce the artifact, not a plan to produce it.",
        "Optimize for fewer tokens and fewer retries: do the smallest complete thing that satisfies the brief.",
        "Use tools where they help; state what evidence you checked before acting.",
        "Parallelize with subagents where independent work exists; merge with a single coherent voice.",
        "Keep a searchable working note so the task survives context compaction.",
        "Compare against the provided reference and fix the largest gaps first.",
    ][i % 6]
    effort_line = (
        f" {model['level_label']}: `{effort}`. {model['control']}"
        if effort
        else f" {model['control']}"
    )
    article = "an" if role.split()[0][0].lower() in "aeiou" else "a"
    task_sent = task[0].upper() + task[1:] if task else task
    prompt = (
        f"Target model: {model['display']} ({model['model_id']}). "
        f"Act as {article} {role}. {task_sent} {aud}. "
        f"The intended result is {out}. "
        f"Requirements: {con}; {con2}. {angle}{effort_line} "
        f"{autonomy} {verify}"
    )
    prompt = " ".join(prompt.split())
    return dict(
        role=role,
        task=task,
        audience=aud,
        constraints=[con, con2],
        output=out,
        autonomy=autonomy,
        verification=verify,
        effort=effort,
        text=prompt,
    )


def generate_one(model):
    out_root = ROOT / "models" / model["slug"]
    prompts_dir = out_root / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)

    all_rows = []
    for cat in CATEGORIES:
        seen = set()
        rows = []
        for i in range(PER_CATEGORY):
            p = build_prompt(cat, i, model)
            h = hashlib.sha256(p["text"].encode()).hexdigest()
            if h in seen:
                p["text"] = p["text"] + f" Variant focus {i + 1}."
                h = hashlib.sha256(p["text"].encode()).hexdigest()
            seen.add(h)
            pid = (
                f"{cat['slug'][3:]}-{i + 1:03d}"
                if cat["slug"][:2].isdigit()
                else f"{cat['slug']}-{i + 1:03d}"
            )
            rows.append(
                {"id": pid, "category": cat["slug"], "title": cat["title"], **p}
            )
        for r in rows:
            all_rows.append(r)

    texts = [r["text"] for r in all_rows]
    assert len(texts) == len(set(texts)), (
        f"Duplicate prompts for {model['slug']}: {len(texts) - len(set(texts))}"
    )
    print(f"[{model['slug']}] Total prompts: {len(all_rows)} unique OK")

    def to_vertical(text):
        sentences = [s.strip() for s in text.split(". ") if s.strip()]
        fixed = []
        for s in sentences:
            if not s.endswith("."):
                s = s + "."
            fixed.append(textwrap.fill(s, width=100))
        return "\n".join(fixed)

    for cat in CATEGORIES:
        rows = [r for r in all_rows if r["category"] == cat["slug"]]
        md = []
        md.append(
            f"# {cat['emoji']} {cat['title']} - 120 copyable {model['display']} prompts\n"
        )
        md.append(f"> {cat['desc']}\n")
        md.append(
            f"> Target model: {model['display']} (`{model['model_id']}`). {model['control']}\n"
        )
        md.append(
            "> Safety: defensive / authorized-scope use only. Stop before destructive, irreversible, sending, purchasing, deleting, or permission-changing steps without approval.\n"
        )
        md.append(
            f"**Jump:** [Model index](../../README.md) · [Search all](prompts_index.json)\n"
        )
        md.append(
            "How to use: click any prompt title to expand it top to bottom, then use the copy icon on the code block.\n"
        )
        for r in rows:
            short_task = r["task"][:72]
            md.append(
                f"<details>\n<summary><code>{r['id']}</code> - {short_task} (click to expand)</summary>\n"
            )
            md.append("```text")
            md.append(to_vertical(r["text"]))
            md.append("```\n</details>\n")
        (prompts_dir / f"{cat['slug']}.md").write_text("\n".join(md), encoding="utf-8")

    with open(prompts_dir / "prompts.jsonl", "w", encoding="utf-8") as f:
        for r in all_rows:
            f.write(
                json.dumps(
                    {"id": r["id"], "category": r["category"], "prompt": r["text"]},
                    ensure_ascii=False,
                )
                + "\n"
            )
    with open(prompts_dir / "prompts.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "category", "prompt"])
        w.writeheader()
        for r in all_rows:
            w.writerow({"id": r["id"], "category": r["category"], "prompt": r["text"]})
    index = [
        {
            "id": r["id"],
            "category": r["category"],
            "title": r["title"],
            "task": r["task"],
        }
        for r in all_rows
    ]
    (prompts_dir / "prompts_index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    manifest = [
        {
            "slug": c["slug"],
            "emoji": c["emoji"],
            "title": c["title"],
            "desc": c["desc"],
            "count": PER_CATEGORY,
        }
        for c in CATEGORIES
    ]
    (out_root / "categories.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8"
    )

    # per-model README
    readme = f"""# {model["display"]} Prompt Pack

**{PER_CATEGORY * len(CATEGORIES):,} copy-paste prompts** across {len(CATEGORIES)} categories, tuned for `{model["model_id"]}`.

- Model: `{model["model_id"]}`
- Strengths: {model["strengths"]}
- Control: {model["control"]}
- Levels: {", ".join(model["levels"])}

## Contents
- `prompts/` - 28 category markdown files (120 prompts each) plus `prompts.jsonl`, `prompts.csv`, `prompts_index.json`
- `categories.json` - category manifest

Generated by `scripts/generate_model_prompts.py`.
"""
    (out_root / "README.md").write_text(readme, encoding="utf-8")
    print(f"[{model['slug']}] Wrote markdown, jsonl, csv, index, manifest, README.")


def main():
    args = sys.argv[1:] or ["all"]
    targets = MODELS if "all" in args else [m for m in MODELS if m["slug"] in args]
    for m in targets:
        generate_one(m)
    # root models index
    idx_path = ROOT / "models" / "README.md"
    (ROOT / "models").mkdir(parents=True, exist_ok=True)
    lines = [
        "# Frontier Model Prompt Packs\n",
        "Multi-model prompt library. Each pack contains 28 categories x 120 prompts.\n",
    ]
    lines.append("| Model | Slug | Prompts | Strengths |")
    lines.append("|---|---|---|---|")
    for m in MODELS:
        lines.append(
            f"| {m['display']} | `{m['slug']}` | {PER_CATEGORY * len(CATEGORIES):,} | {m['strengths']} |"
        )
    lines.append("")
    lines.append("See also the GPT-6 Astra pack at the repository root (`prompts/`).\n")
    idx_path.write_text("\n".join(lines), encoding="utf-8")
    print("Wrote models/README.md")


if __name__ == "__main__":
    main()
