import json
from flask import Flask, render_template, request

from led_matrix.display_handler import DisplayHandler

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/command", methods=["POST"])
def command():
    if request.form:
        c_id = DisplayHandler.command(dict(request.form))

        if c_id:
            data = DisplayHandler.wait_complete()

            if not data or c_id != data["uuid"]:
                return "ERROR"

            return json.dumps(data["response"])

    return "False"

@app.route("/randomize", methods=["POST"])
def randomize():
    return "True"
