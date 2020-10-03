from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def logistics():
    return render_template("logistics.html")


@app.route('/Logistic_Companies')
def companies():
    return render_template("companies.html")

