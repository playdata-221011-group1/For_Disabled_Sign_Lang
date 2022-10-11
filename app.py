from flask import Flask, render_template

app = Flask(__name__)

#메인페이지
@app.route("/")
def index():

    return render_template("index.html")