from flask import Flask, render_template
import json

app = Flask(__name__)

file = open("pln-2324\TPC6\conceitos2.json", encoding="utf-8")
conceitos=json.load(file)
 
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/conceitos")
def listar_conceitos():
    return render_template("conceitos.html",conceitos=conceitos)

@app.route("/conceitos/<id>")
def consultar_Conceito(id):
    return render_template("conceito.html",c=id, conceito=conceitos[id])

if __name__ == "__main__":
    app.run(debug=True)