from flask import Flask, render_template
from pathlib import Path
import markdown

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
REASONING_FILE = BASE_DIR / "reasoning.md"

def read_markdown_file() -> str:
    if not REASONING_FILE.exists():
        REASONING_FILE.write_text("# Why We’re Leaving Discord\n\nWrite here...\n", encoding="utf-8")
    return REASONING_FILE.read_text(encoding="utf-8")

@app.get("/")
def index():
    md_text = read_markdown_file()

    # Markdown -> HTML
    html = markdown.markdown(
        md_text,
        extensions=[
            "extra",        # tables, fenced code blocks, etc.
            "sane_lists",
            "toc",
            "nl2br",        # respects newlines more nicely
        ],
        output_format="html5",
    )

    return render_template("index.html", content_html=html)

if __name__ == "__main__":
    app.run(debug=True)
