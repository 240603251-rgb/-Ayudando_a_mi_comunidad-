from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/adopcion")
def adopcion():
    return render_template('adopcion.html')

@app.route("/contacto")
def contacto():
    return render_template('contacto.html')

@app.route("/faq")
def faq():
    return render_template('faq.html')

@app.route("/revision")
def revision():
    return render_template('revision.html')