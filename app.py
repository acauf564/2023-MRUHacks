from flask import Flask, render_template, request
from PDFtoLIST import *
from mainController import *

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['']
        f.save('/var/www/uploads/uploaded_file.pdf')

app.run(debug=True)


