from flask import Flask, render_template, request
import json
import os
import shutil

app = Flask(__name__)

file = open("pln-2324\TPC7\documentos\conceitos2.json", encoding="utf-8")
conceitos=json.load(file)
 
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/conceitos")
def listar_conceitos():
    return render_template("conceitos.html",conceitos=conceitos)

@app.route("/conceitos/<id>")
def consultar_Conceito(id):
    if id in conceitos:
        return render_template("conceito.html",c=id, conceito=conceitos[id])
    else:
        return render_template("erro.html", erro="Conceito não existente na base de dados.")
    
@app.route("/conceitos", methods=["POST"])
def adicionar_conceitos():
    designacao=request.form.get("designacao")
    descricao=request.form.get("descricao")
    en=request.form.get("en")
    
    conceitos[designacao]={"desc":descricao, "en": en}
    
    return render_template("conceitos.html",conceitos=conceitos)

@app.route("/conceitos/<designacao>", methods=["DELETE"])
def delete_conceitos(designacao):
    # Criar uma cópia de backup do arquivo original
    shutil.copy("pln-2324\TPC7\documentos\conceitos2.json", "pln-2324\TPC7\documentos\conceitos_backup.json")

    # Abrir o arquivo original para leitura
    with open("pln-2324\TPC7\documentos\conceitos2.json", encoding="utf-8") as file:
        conceitos = json.load(file)

    # Deletar o conceito
    if designacao in conceitos:
        del conceitos[designacao]
        print(conceitos)

        # Abrir o arquivo original para escrita
        with open("pln-2324\TPC7\documentos\conceitos2.json", "w", encoding="utf-8") as file_out:
            try:
                # Escrever os dados atualizados no arquivo
                json.dump(conceitos, file_out, ensure_ascii=False)
            except Exception as e:
                # Se ocorrer um erro, restaurar o arquivo original a partir da cópia de backup
                shutil.copy("pln-2324\TPC7\documentos\conceitos_backup.json", "pln-2324\TPC7\documentos\conceitos2.json")
                return render_template("erro.html", erro="Ocorreu um erro ao atualizar os conceitos. O arquivo original foi restaurado.")

        # Retornar o template com os conceitos atualizados
        return render_template("conceitos.html", conceitos=conceitos)
    else:
        return render_template("erro.html", erro="Conceito não existente na base de dados.")


@app.route("/tabela")
def table():
    return render_template("table.html", conceitos=conceitos)

@app.route("/pesquisa", methods=["GET", "POST"])
def search():
    termo = request.form.get("termo", "") if request.method == "POST" else ""
    if request.method == "POST":
        resultados_pesq = {}
        for chave, valor in conceitos.items():
            if termo.lower() in chave.lower():
                resultados_pesq[chave] = valor
        return render_template("pesquisa.html", resultados_pesq=resultados_pesq, termo=termo)
    
    # Se a solicitação for GET ou se não houver resultados, retorne a página de pesquisa com termo vazio
    return render_template("pesquisa.html", resultados_pesq={}, termo=termo)


if __name__ == "__main__":
    app.run(debug=True)