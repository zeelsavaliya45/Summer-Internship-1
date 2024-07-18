from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("insert.html", content= ["zeel", "parth", "Grensi"])

if __name__ == "__main__":
    app.run()