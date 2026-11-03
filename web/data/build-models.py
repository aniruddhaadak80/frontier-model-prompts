"""Build the model-pack index for the showcase.

Reads every model pack under ../models plus the root Astra pack and writes
data/models.json. Run from web/: py data/build-models.py
"""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REPO = "https://github.com/aniruddhaadak80/frontier-model-prompts"

META = {
    "gpt-6-astra": {
        "display": "GPT-6 Astra",
        "vendor": "OpenAI",
        "context": "1.05M",
        "strengths": "Agentic coding, 3D, computer use, long context",
        "path": "prompts",
    },
    "opus-5-5": {
        "display": "Claude Opus 5.5",
        "vendor": "Anthropic",
        "context": "1M",
        "strengths": "Long-running agentic coding, vision, computer use",
        "path": "models/opus-5-5/prompts",
    },
    "gemini-4-argon": {
        "display": "Gemini 4 Argon",
        "vendor": "Google DeepMind",
        "context": "1M",
        "strengths": "Deep visual perception, finance/legal, cybersecurity",
        "path": "models/gemini-4-argon/prompts",
    },
    "muse-wonder": {
        "display": "Muse Wonder",
        "vendor": "Meta",
        "context": "long",
        "strengths": "Active memory, goal persistence, agentic tasks",
        "path": "models/muse-wonder/prompts",
    },
    "kimi-k-3-1": {
        "display": "Kimi K 3.1 Pro",
        "vendor": "Moonshot",
        "context": "1M",
        "strengths": "Coding agents, 3D generation, open weights",
        "path": "models/kimi-k-3-1/prompts",
    },
    "deepseek-v3-2": {
        "display": "DeepSeek V3.2",
        "vendor": "DeepSeek",
        "context": "128K",
        "strengths": "Coding, math, open weights, cost-efficient",
        "path": "models/deepseek-v3-2/prompts",
    },
    "grok-4": {
        "display": "Grok 4",
        "vendor": "xAI",
        "context": "256K",
        "strengths": "Real-time web, reasoning, multimodal",
        "path": "models/grok-4/prompts",
    },
    "qwen-3": {
        "display": "Qwen 3",
        "vendor": "Alibaba",
        "context": "128K",
        "strengths": "Multilingual, coding, open weights",
        "path": "models/qwen-3/prompts",
    },
    "llama-4": {
        "display": "Llama 4",
        "vendor": "Meta",
        "context": "10M",
        "strengths": "Open weights, long context, multimodal",
        "path": "models/llama-4/prompts",
    },
    "mistral-large-3": {
        "display": "Mistral Large 3",
        "vendor": "Mistral AI",
        "context": "256K",
        "strengths": "Multilingual, coding, function calling, open weights",
        "path": "models/mistral-large-3/prompts",
    },
    "glm-5": {
        "display": "GLM-5",
        "vendor": "Zhipu AI",
        "context": "long",
        "strengths": "Agentic coding, reasoning, open weights",
        "path": "models/glm-5/prompts",
    },
}


def pack_entry(slug, base):
    cats = json.loads((base / "categories.json").read_text(encoding="utf-8"))
    jsonl = base / "prompts" / "prompts.jsonl"
    count = sum(
        1 for line in jsonl.read_text(encoding="utf-8").splitlines() if line.strip()
    )
    meta = META[slug]
    return {
        "slug": slug,
        "display": meta["display"],
        "vendor": meta["vendor"],
        "context": meta["context"],
        "strengths": meta["strengths"],
        "prompts": count,
        "categories": len(cats),
        "url": REPO + "/tree/main/" + meta["path"],
    }


def main():
    packs = [pack_entry("gpt-6-astra", ROOT)]
    for model_dir in sorted((ROOT / "models").iterdir()):
        if not model_dir.is_dir() or not (model_dir / "categories.json").exists():
            continue
        if model_dir.name not in META:
            continue
        packs.append(pack_entry(model_dir.name, model_dir))
    packs.sort(key=lambda p: p["display"].lower())
    (HERE / "models.json").write_text(
        json.dumps(packs, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    print(f"wrote {len(packs)} model packs, {sum(p['prompts'] for p in packs)} prompts")


if __name__ == "__main__":
    main()
