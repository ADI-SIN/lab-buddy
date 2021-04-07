from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)

# Global variable block


# Blobal Classes block


# Helper functions block


# Endpoints block


@app.route("/", methods=["GET"])
def home():
    return "Welcome to Lab Buddy"


@app.route("/findtopic")
def new_student():
    return render_template("video.html")


@app.route("/gettopic", methods=["POST", "GET"])
def findvideos():
    if request.method == "POST":
        try:
            topic = request.form["nm"]
            print("Topic: "+topic)
            obj = Database()
            msg = obj.list_topic(topic)
        except Exception as e:
            msg = "error in fetch operation" + str(e)
            return render_template("list.html", msg=msg)

        #return msg
        print(msg)
        return render_template("list.html", msg=msg)


# API runner
app.run(host="0.0.0.0", debug=True, port=9898)
