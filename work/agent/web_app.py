"""
FL-09: ResearchScout Agent — Flask Web Application Server
Exposes:
  GET  /           -> Premium Web UI (templates/index.html)
  POST /api/research -> JSON: { query } -> { brief_markdown, metadata, saved_path, elapsed_ms }
"""

import os
import sys
import time
import json

# Add parent directory to path so we can import research_scout
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, jsonify, render_template
from research_scout import ResearchScoutAgent

# ---------------------------------------------------------------------------
# App Initialisation
# ---------------------------------------------------------------------------
TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
app = Flask(__name__, template_folder=TEMPLATES_DIR)

# Single shared agent instance (output goes to standard research_briefs folder)
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "outputs", "research_briefs"
)
agent = ResearchScoutAgent(output_dir=OUTPUT_DIR)

# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Serve the premium Web UI."""
    return render_template("index.html")


@app.route("/api/research", methods=["POST"])
def research():
    """
    POST /api/research
    Body (JSON): { "query": "<arXiv ID or topic string>" }
    Returns (JSON): {
        "success": bool,
        "query": str,
        "metadata": { title, authors, published, arxiv_url, pdf_url, paper_id },
        "brief_markdown": str,
        "saved_path": str,
        "elapsed_ms": int,
        "error": str  (only on failure)
    }
    """
    body = request.get_json(silent=True) or {}
    query = (body.get("query") or "").strip()

    if not query:
        return jsonify({"success": False, "error": "Query is required."}), 400

    start = time.time()
    try:
        # Step 1 — Live Tool 1: arXiv REST API fetch
        metadata = agent.fetch_arxiv_paper(query)

        # Step 2 — Core Job: Synthesis
        brief_md = agent.synthesize_research_brief(metadata)

        # Step 3 — Live Tool 2: Filesystem persistence
        clean_filename = f"arxiv_{metadata['paper_id'].replace('.', '_')}_brief.md"
        saved_path = agent.save_brief_to_file(clean_filename, brief_md)

        elapsed_ms = round((time.time() - start) * 1000)

        return jsonify({
            "success": True,
            "query": query,
            "metadata": {
                "paper_id":  metadata["paper_id"],
                "title":     metadata["title"],
                "authors":   metadata["authors"],
                "published": metadata["published"],
                "arxiv_url": metadata["arxiv_url"],
                "pdf_url":   metadata["pdf_url"],
            },
            "brief_markdown": brief_md,
            "saved_path":     saved_path,
            "elapsed_ms":     elapsed_ms,
        })

    except ValueError as ve:
        return jsonify({"success": False, "query": query, "error": str(ve)}), 404
    except Exception as exc:
        return jsonify({"success": False, "query": query, "error": str(exc)}), 500


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("  ResearchScout Agent — Web UI Server")
    print("  http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, port=5000, use_reloader=False)
