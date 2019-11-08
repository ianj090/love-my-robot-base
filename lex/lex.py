from flask import Flask, render_template, request
import requests, sys

app = Flask(__name__)

f = open("transpiled/test.py", "w+")
for i in range(10):
    f.write("Test Line %d\r\n" % (i+1))
f.close()

@app.route("/")
def translation():
    return render_template(
        "translated.html",
    )

@app.route("/lex")
def lex():
    return "POST endpoint"

if __name__ == "__main__":
    app.run(host="0.0.0.0")