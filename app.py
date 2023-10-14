from flask import Flask, render_template, request
from PDFtoLIST import *
from mainController import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scanner")
def scanner():
    return render_template("scanner.html")

@app.route("/taskmanager")
def taskmanager():
    return render_template("taskmanager.html")


@app.route("/scannersubmit")
def scannersubmit():
    return render_template("scanner.html", table=main())



# @app.route('/upload')
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['']
#         f.save('/var/www/uploads/uploaded_file.pdf')
if __name__ == '__main__':
    app.run(debug=True)


