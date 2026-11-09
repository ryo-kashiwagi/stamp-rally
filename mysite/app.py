from flask import Flask, render_template

app = Flask(__name__)

@app.route("/camera")
def camera_page():
    return render_template("camera_page/index.html")

@app.route("/gallery")
def gallery_page():
    return render_template("gallery_page/index.html")