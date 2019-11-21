from flask import Flask, render_template, request
import requests, sys, json

app = Flask(__name__)

# get = requests.get('http://localhost:8080/getdata') # GET request
# print(get.request.body)
# data = get.json()
# # process this JSON data and do something with it
# print(data)


# if data != "":
#     result = {"status": "SUCCESSFUL"}
# else:
#     result = {"status": "FAILED"}
 
# now immediately sending a post request with new data
# post = requests.post('http://127.0.0.1:8080/postdata', json=result) # the POST request
# print(post.text)
# print(result)

f = open("transpiled/test.py", "w+")
for i in range(10):
    f.write("Test Line %d\r\n" % (i+1))
f.close()

@app.route("/")
def translation():
    return render_template(
        "translated.html",
    )

@app.route("/lex", methods=["POST"])
def lex():
    data = request.get_json()
    print(data)
    # do something with this data variable that contains the data from the node server
    return json.dumps({"Connection":"Succesful"})

if __name__ == "__main__":
    app.run(host="0.0.0.0")