from flask import Flask, render_template, request
import requests, sys

app = Flask(__name__)


@app.route("/")
def translation():
    return render_template(
        "layout.html"
    )

@app.route("/lex")
def lex():
    return "Operations"

if __name__ == "__main__":
    app.run(host="0.0.0.0")