from pathlib import Path

from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

STATUS_FILE = Path(__file__).with_name("hand_status.txt")
DEFAULT_STATE = "разжата"
VALID_STATES = {"сжата", "разжата"}


def load_hand_state():
    if not STATUS_FILE.exists():
        return DEFAULT_STATE

    state = STATUS_FILE.read_text(encoding="utf-8").strip()
    if state in VALID_STATES:
        return state

    return DEFAULT_STATE


def save_hand_state(state):
    STATUS_FILE.write_text(state + "\n", encoding="utf-8")


hand_state = load_hand_state()


@app.route("/")
def index():
    return render_template("index.html", hand_state=hand_state)


@app.route("/on")
def on():
    global hand_state
    hand_state = "сжата"
    save_hand_state(hand_state)
    return redirect(url_for("index"))


@app.route("/off")
def off():
    global hand_state
    hand_state = "разжата"
    save_hand_state(hand_state)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
