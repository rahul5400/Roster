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
    return render_template("home.html", examples=EXAMPLES, members=None, error=None)


@app.post("/")
def load():
    body = request.form.get("roster") or ""
    if not body.strip():
        return render_template(
            "home.html",
            examples=EXAMPLES,
            members=None,
            error="Paste a roster.",
        ), 400
    try:
        loaded = yaml.safe_load(body)
    except yaml.YAMLError:
        return render_template(
            "home.html",
            examples=EXAMPLES,
            members=None,
            error="That roster could not be read.",
        ), 400
    if not isinstance(loaded, list) or not loaded or any(
        not isinstance(person, dict)
        or not isinstance(person.get("name"), str)
        or not person["name"].strip()
        or not isinstance(person.get("role"), str)
        or not person["role"].strip()
        for person in loaded
    ):
        return render_template(
            "home.html",
            examples=EXAMPLES,
            members=None,
            error="Use a YAML list where every person has a name and role.",
        ), 400
    return render_template(
        "home.html",
        examples=EXAMPLES,
        members=loaded,
        error=None,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "3000")))
