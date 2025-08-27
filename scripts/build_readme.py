import datetime
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.yml"
ASSETS = ROOT / "assets"
README = ROOT / "README.md"

MARK_START = "<!--CHART_START-->"
MARK_END = "<!--CHART_END-->"


def load_papers():
    with open(DATA, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def make_bar_chart(counts, outpath):
    ASSETS.mkdir(exist_ok=True, parents=True)
    categories = list(counts.keys())
    values = [counts[c] for c in categories]

    plt.figure(figsize=(6, 3.6))
    plt.bar(categories, values)
    plt.title("Papers by Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(outpath, format=outpath.suffix.lstrip("."), dpi=200)
    plt.close()


def render_table_md(counts, total):
    lines = ["\n**Breakdown**", "", "| Category | Count |", "|---|---|"]
    for k, v in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0].lower())):
        lines.append(f"| {k} | {v} |")
    lines.append(f"| **Total** | **{total}** |")
    return "\n".join(lines)


def make_recent_list_md(papers, limit=10):
    def parse_date(d):
        try:
            return datetime.date.fromisoformat(d)
        except Exception:
            return datetime.date.min

    sorted_papers = sorted(
        papers, key=lambda p: parse_date(p.get("date", "")), reverse=True
    )
    items = []
    for p in sorted_papers[:limit]:
        title = p.get("title", "(no title)")
        cat = p.get("category", "-")
        date = p.get("date", "")
        link = p.get("link", "")
        if link:
            items.append(f"- [{title}]({link}) — *{cat}* ({date})")
        else:
            items.append(f"- {title} — *{cat}* ({date})")
    return "\n".join(["\n**Recently read**", ""] + items) if items else ""


def update_readme(chart_rel_path, table_md, recent_md):
    md = README.read_text(encoding="utf-8")
    start = md.find(MARK_START)
    end = md.find(MARK_END)
    if start == -1 or end == -1 or end < start:
        raise RuntimeError("Markers not found in README.md")

    insert_md = "\n".join(
        [f"![Category chart]({chart_rel_path})", "", table_md, recent_md]
    )

    new_md = md[: start + len(MARK_START)] + "\n" + insert_md + "\n" + md[end:]
    README.write_text(new_md, encoding="utf-8")


def main():
    papers = load_papers()
    counts = Counter([p.get("category", "Unknown") for p in papers])
    total = sum(counts.values())

    chart_path = ASSETS / "category_counts.svg"
    make_bar_chart(counts, chart_path)

    table_md = render_table_md(counts, total)
    recent_md = make_recent_list_md(papers, limit=10)

    update_readme(
        chart_rel_path=str(Path("assets") / chart_path.name),
        table_md=table_md,
        recent_md=recent_md,
    )


if __name__ == "__main__":
    main()
