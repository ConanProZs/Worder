from flask import Flask, render_template, url_for, request, redirect
from database import DeleteAll, getAll, insert
from dotenv import load_dotenv
from os import getenv


load_dotenv()
app = Flask(__name__)





@app.route("/ideas/")
def ideas():
    return getAll()

@app.route("/ideas/delete/", methods = ['POST', 'GET'])
def ideas_del():
    if request.method == "POST":
        password = request.form['password']
        if password == getenv("DELETEPASSWORD"):
            DeleteAll()
            return render_template("ideas_del.html")
    else:
        return render_template("ideas_del.html")


@app.route("/")
def index():
    return render_template("main.html")


@app.route('/submitted/', methods = ['POST', 'GET'])
def submitted():
    if request.method == "POST":

        email = request.form['email']
        name = request.form['name']
        word = request.form['word']
        wordpro = request.form['wordpro']
        wordmening = request.form['wordmening']
        insert(email, name, word, wordpro, wordmening)

        return render_template("submitted.html", wordname = word)

    else:
        return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=False)