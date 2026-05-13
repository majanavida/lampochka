from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

bulb_state = "off"


@app.route("/")
def index():
    return render_template("index.html", bulb_state=bulb_state)


@app.route("/button_on")
def button_on():
    global bulb_state
    bulb_state = "on"
    return redirect(url_for("index"))


@app.route("/button_off")
def button_off():
    global bulb_state
    bulb_state = "off"
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
