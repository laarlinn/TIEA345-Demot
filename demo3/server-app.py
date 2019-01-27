from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
    try:
        img = open("../latest.jpg")
        return send_file("../latest.jpg", mimetype="image/jpg")
    except:
        return "Image doesn't exist!"

app.run(host= '0.0.0.0')