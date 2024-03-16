import json
import re
from deep_translator import GoogleTranslator
import os

file_conceitos=open("pln-2324/TPC5/documentos/conceitos.json", encoding="utf-8")
file_livro=open("pln-2324/TPC5/documentos/LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding="utf-8")

texto=file_livro.read()
conceitos=json.load(file_conceitos)

if os.path.exists("pln-2324/TPC5/documentos/dicionarioM_pt_en.json"):
    # Se o arquivo existe, carrega os dados
    with open("pln-2324/TPC5/documentos/dicionarioM_pt_en.json", "r", encoding="utf-8") as dicionario_trad_pt_en:
        dic_trad = json.load(dicionario_trad_pt_en)
else:
    # Se o arquivo não existe, cria o dicionário vazio
    dic_trad={}

    for designacao_pt in conceitos:
        designacao_en = GoogleTranslator(source='pt', target='en').translate(designacao_pt)
        dic_trad[designacao_pt]={"desc": conceitos[designacao_pt],
                                "en": designacao_en}

    dicionario= open("pln-2324/TPC5/documentos/dicionarioM_pt_en.json","w", encoding="utf-8")
    json.dump(dic_trad, dicionario, indent=4, ensure_ascii=False)

blacklist=["este","e","para","de","pelo","os","são"]
dic_trad_min={chave.lower(): dic_trad[chave] for chave in conceitos}

#conceitos_min={chave.lower(): conceitos[chave].lower() for chave in conceitos}

print(dic_trad_min)

def etiquetador(m):
    palavra=m[0]
    original=palavra
    palavra= palavra.lower()
    if palavra in dic_trad_min and palavra not in blacklist:
        descricao = dic_trad_min[palavra]['desc']  # Acessando a descrição em português
        designacao_en = dic_trad_min[palavra]['en']  # Acessando a descrição em inglês
        etiqueta = f"<a href='' title='{designacao_en}\n{descricao}'>{original}</a>"
        return etiqueta
    else:
        return original

regex= r"[\wàéáíõãêú]+"
texto = re.sub(r"\n",r"<br>",texto)
texto = re.sub(r"\f",r"<hr>",texto)
texto = re.sub(regex ,etiquetador,texto, flags=re.IGNORECASE)

output_file= open("pln-2324/TPC5/livro_com_conceitos.html", "w", encoding="utf-8")
print(texto,file=output_file)

print("Arquivo HTML criado com sucesso: livro_com_conceitos.html")