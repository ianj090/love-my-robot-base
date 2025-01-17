from flask import Flask, render_template, request
import requests
import sys
import json
import command

app = Flask(__name__)

# f = open("transpiled/test.py", "w+")
# for i in range(10):
#     f.write("Test Line %d\r\n" % (i+1))
# f.close()

time_stamp = ""
translatedcode = ""


@app.route("/")
def translation():
    return render_template(
        "lex.html",
        timestamp=time_stamp,
        code=translatedcode
    )


@app.route("/lex", methods=["POST"])  # solo va a ACEPTAR post
def lex():  # Todas las operaciones van a pasar aqui!!!
    data = request.get_json()
    print(data)
    global time_stamp
    global translatedcode
    time_stamp = data["request_timestamp"]
    translation()
    translatedcode = command.interpret(data)
    print(translatedcode)
    # do something with this data variable that contains the data from the node server
    return json.dumps({"Connection": "Succesful"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
