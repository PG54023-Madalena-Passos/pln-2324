# 1. dada uma string s, revertê-la
def reverse (s):
    s_reversed=s[::-1]
    return s_reversed

print(reverse("OLÁ"))

# 2. dada uma string s, retornar quantos caracteres a e A estão presentes na mesma
def count_characters(s):
    c_a=s.count("a")
    c_A=s.count("A")

    return c_a,c_A

print(count_characters("OlaaAAA"))

# 3. dada uma string s, retornar o número de vogais que estão presentes na mesma
def count_vowels(s):
    vowels=["a","e","i","o","u"]
    c_v=0
    for l in s:
        if l in vowels:
            c_v+=1
    
    return c_v

print(count_vowels("ola"))

# 4. dada uma string s, convertê-la para letra minúscula
def conv_lower(s):
    s_l=s.lower()
    return s_l

print(conv_lower("OLA"))

# 5. dada uma string s, convertê-la para letra maiúscula
def conv_upper(s):
    s_u=s.upper()
    return s_u

print(conv_upper("ola"))

# 6. Verifica se uma string é capicua
def e_capicua(s):
    capicua=False
    inv_s=s[::-1]
    if s==inv_s:
        capicua=True

    return capicua

print(e_capicua("1221"))
print(e_capicua("1231"))

# 7. Verifica se duas strings estão balanceadas (2 strings são balanceadas se todos os caracteres de s1 
#     estão presentes em s2)
def e_balanceada(s1,s2):
    for l1 in s1:
        if l1 not in s2:
            return False
    return True

print(e_balanceada("a","ola"))
print(e_balanceada("ola","la"))

# 8. Calcula o numero de ocorrencias de s1 e s2
def ocorrencias(s1,s2):
    c_oc=s2.count(s1)
    return c_oc

print(ocorrencias("o","olaola"))

# 9. Verifica se s1 é anagrama de s2
def e_anagrama(s1,s2):
    bal=e_balanceada(s1,s2)
    if bal==True and len(s1)==len(s2):
        return True
    return False

print(e_anagrama("silent","listen"))
print(e_anagrama("hello","world"))

# 10. Dado um dicionário, calcular a tabela das classes de anagramas

# Lêr o ficheiro
filename= "C:/Users/Carla Passos/Desktop/MIEBIOM/PLN/aulas/CIH Bilingual Medical Glossary English-Spanish.txt"
f=open(filename, 'r', encoding='utf-8')
text=f.read()

# Pré-processamento dos dados (remoção dos caracteres ",",".","-","/","©","/a",")" e "(")
text= text.replace(","," ")
text= text.replace("."," ")
text= text.replace("-"," ")
text= text.replace("/"," ")
text= text.replace("©"," ")
text= text.replace("/a"," ")
text= text.replace(")"," ")
text= text.replace("("," ")

# separar o texto que se encontrava corrido em palavras
tokens=text.split()

# uniformizar o texto, transformando todas as letras em minúsculas
text=text.lower()

# dicionário para guardar os anagramas
anagramas={}

tokens=list(set(tokens)) # para retirar repetidos

# criar uma chave com as letras das palavra por ordem alfabética
def ordenaLetras(s):
    chave = ''.join(sorted(s))
    return chave

# aplicação da função de ordenação das palavras pelas letras
for token in tokens:
    chv=ordenaLetras(token)
    if chv not in anagramas.keys():
        i=0
        anag_chv=[]
        for i in range(len(tokens)):
            if chv==ordenaLetras(tokens[i]):
                anag_chv.append(tokens[i]) # inserção das palavras na lista relativa às letras em questão
        anagramas[chv]=anag_chv # inserção da palavra no dicionário

# verificação
for chave, palavras in anagramas.items():
    print(f'Classe de Anagramas ({chave}): {palavras}')

# observar existência de mais do que uma palavra como anagramas
for chave, palavras in anagramas.items():
    if len(palavras) > 1:
        print(f'Classe de Anagramas ({chave}): {palavras}')