import re

# Lêr o ficheiro
filename= "pln-2324/TPC3/documentos/dicionario_medico.txt"
f=open(filename, 'r', encoding='utf-8')
texto=f.read()

#Opção 1

#marcar designações
texto=re.sub(r'\n\n(.+)',r'\n\n@\1', texto)

#data cleaning
texto=re.sub(r'@(.+)\n\n@',r'@\1\n',texto)  #Tratar casos de @ na designação e na definição (T1)
texto=re.sub(r'\n\n@\f([A-Za-z]+.+\.)\n(.+)', r' \1\n\n@\2', texto)  #Tratar casos de @ no meio de uma frase, devido à quebra de página (T2)
texto=re.sub(r'\f',"",texto)  #Remoção da Quebra de Página

'''
#Ficheiro de controlo
with open("pln-2324/TPC3/documentos/output.txt", "w") as output_file:
    output_file.write(texto)
'''

termos=[]
termos=re.findall(r'@(.+)\n([^@]+)\n\n', texto) #para não considerar o @ e o \n, usa-se um grupo de captura

#print(termos)

#Gerar HTML
header = "<header style='background-color: #3376b8; color: white; display: flex; align-items: center; justify-content: space-between; padding: 10px; width: 100%;'>"
header += "<div style='display: flex; flex-direction: column;'>"
header += "<h1 style='margin: 0; font-size: 15px;'>Processamento de Linguagem Natural 2023-2024</h1>"
header += "<p style='margin: 0; font-size: 10px;'>Madalena Passos, PG54023</p>"
header += "</div>"
header += "<img src='logo_engenharia.jpg' alt='Imagem' style='width: 50px; height: 26px; align-self: flex-end;'>"
header += "</header>"
titulo="<h1 style='font-family: Arial, sans-serif; text-align: center; color: #3376b8;'> Dicionário Médico </h1>"
descricao="<p style='font-family: Arial, sans-serif; text-align: center;'> Este é um dicionário médico desenvolvido na disciplina de PLN.</p>"
body="<body style='font-family: Arial, sans-serif; margin: 0 120px;'>"
for termo in termos:
    body+= f"<h4><b> {termo[0].strip('@')} </b></h4>"
    body+= f"<p> {termo[1]} </p>"
    body += "<hr style='border-color: #e8e8e8; width: 100%;'/>"
    
body += "</body>"

html= header + titulo + descricao + "</br>" + body
print(html)

file_out=open("pln-2324/TPC3/dicionario_medico.html","w")
file_out.write(html)
file_out.close()

'''
#Opção 2
texto=re.sub(r'\n\n(.+)',r'\n\n@\1', texto)
conceitos=re.split(r'\n{2,}',texto)
termos=[tuple(conceito.split('\n',maxsplit=1)) for conceito in conceitos]
print(termos)
'''