# Roster

A club list you paste in. YAML, a name and a role on each line. Roster reads it and shows the board.

Flask and PyYAML. No database.

## Features

- Paste a roster
- Last semester's names as an example
- Health check at `/health`

## Run locally

Python 3.11+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:3000.

## Run with Docker

```bash
docker compose up --build
```

The app listens on port 3000.

## Project layout

```
app.py                 Routes and the load
templates/home.html    Form and the board
static/style.css
desk.txt               A desk note the page does not show
```

## Assignment notes

Host this somewhere your classmates and instructor can reach. Walk the running app until you can explain:

- what the form accepts
- what a loaded roster looks like versus the example list
- what `app.py` does with the paste before it is shown
- what else is in the repo that the page does not link

Then look for a security defect in the running system, document how to trigger it, and patch it without breaking a normal roster. Submit the hosted URL, a short architecture sketch, the writeup, and the patched repo.
