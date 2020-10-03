# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def logistics():
    return render_template("logistics.html")

@app.route('/Logistic_Companies')
def companies():
    return render_template("companies.html")

if __name__=="__main__":
    app.run()
