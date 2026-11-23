import os

import yaml
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "roster-dev-secret")

EXAMPLES = [
    {"name": "Maya Chen", "role": "shop"},
    {"name": "Jordan Hale", "role": "booth"},
    {"name": "Devon Park", "role": "film"},
]


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/")
def home():
    return render_template("home.html", examples=EXAMPLES, members=None, error=None, raw=None)


@app.post("/")
def load():
    body = request.form.get("roster") or ""
    if not body.strip():
        return render_template(
            "home.html",
            examples=EXAMPLES,
            members=None,
            error="Paste a roster.",
            raw=None,
        ), 400
    try:
        loaded = yaml.load(body, Loader=yaml.Loader)
    except Exception:
        return render_template(
            "home.html",
            examples=EXAMPLES,
            members=None,
            error="That roster could not be read.",
            raw=None,
        ), 400
    members = loaded if isinstance(loaded, list) else None
    raw = None if members is not None else loaded
    return render_template(
        "home.html",
        examples=EXAMPLES,
        members=members,
        error=None,
        raw=raw,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "3000")))
