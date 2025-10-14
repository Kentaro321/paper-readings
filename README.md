# 📚 Paper Reading Log

Track and visualize your paper reading with auto-updated charts.

<!--CHART_START-->
![By category](assets/category_stylish.svg)

![Activity heatmap](assets/activity_heatmap.svg)


**Breakdown**

| Category | Count |
|---|---|
| LLM | 39 |
| Multimodal (T/S) | 31 |
| TTS | 23 |
| NAC | 12 |
| ML | 7 |
| ASR | 5 |
| Multimodal (T/I) | 5 |
| Dataset (Speech) | 4 |
| Speech | 4 |
| Multimodal (T/S/I/V) | 3 |
| ST | 2 |
| VC | 2 |
| Audio | 1 |
| Image | 1 |
| Multimodal (T/S/I) | 1 |
| Multimodal Generation | 1 |
| NV | 1 |
| Text Embedding | 1 |
| THG | 1 |
| TTI | 1 |
| **Total** | **145** |

**Recently read**

- [Full-Duplex-Bench-v2: A Multi-Turn Evaluation Framework for Duplex Dialogue Systems with an Automated Examiner](https://arxiv.org/abs/2510.07838) — *Multimodal (T/S)* (2025-10-14)
- [Byte Latent Transformer: Patches Scale Better Than Tokens](https://aclanthology.org/2025.acl-long.453.pdf) — *LLM* (2025-10-13)
- [Mamba-3: Improved Sequence Modeling using State Space Principles](https://openreview.net/pdf?id=HwCvaJOiCj) — *LLM* (2025-10-12)
- [SHANKS: Simultaneous Hearing and Thinking for Spoken Language Models](https://arxiv.org/abs/2510.06917) — *Multimodal (T/S)* (2025-10-11)
- [Less is More: Recursive Reasoning with Tiny Networks](https://arxiv.org/abs/2510.04871) — *ML* (2025-10-10)
- [Latent Speech-Text Transformer](https://arxiv.org/abs/2510.06195) — *Multimodal (T/S)* (2025-10-09)
- [KAME: Tandem Architecture for Enhancing Knowledge in Real-Time Speech-to-Speech Conversational AI](https://arxiv.org/abs/2510.02327) — *Multimodal (T/S)* (2025-10-08)
- [Self-Improvement in Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2510.02665) — *Multimodal (T/I)* (2025-10-07)
- [ExGRPO: Learning to Reason from Experience](https://arxiv.org/abs/2510.02245) — *LLM* (2025-10-06)
- [Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation](https://arxiv.org/abs/2509.25849) — *LLM* (2025-10-03)
<!--CHART_END-->

## How to add a new paper

Add paper info to `data/papers.yml` in the following format:

```yaml
- title: "Your paper title"
  category: "LLM"
  date: "YYYY-MM-DD"
  link: "https://..."
```

## Reuse This Repo

- Use as template: Click "Use this template" on GitHub, then edit `data/papers.yml`.
- Timezone: Set `PAPERS_TZ` in the workflow (default `Asia/Tokyo`).
- CI validation: The workflow validates `data/papers.yml` before building charts.
- Export: CI also writes a machine-readable `data/papers.json` for reuse.

See `TEMPLATE.md` for details.

## Development

With `uv` (recommended):

```
uv sync
uv run scripts/validate_papers.py
uv run scripts/build_readme.py
uv run scripts/export_json.py
```

## License

- Code: MIT (`LICENSE`)
- Content (notes, `data/papers.yml`, generated charts in `assets/`): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
