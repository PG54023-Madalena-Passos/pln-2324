## Trabalho de casa 1

Neste exercício prático, era pretendida a resolução de 14 enunciados relacionados com a utilização de expressões regulares.

Expressões regulares, comumente conhecidas como "regex", são padrões de texto utilizados para realizar correspondências e manipulações em _strings_. Esses padrões são representados por sequências de caracteres que definem um conjunto de regras de procura.

### Procedimento
Para a realização deste trabalho, foi importada a biblioteca de _python_ **re** e, posteriormente, executados os seguintes passos.

#### 1.1. Dada uma linha de texto, definir um programa que determina se a palavra "hello" aparece no início da linha.
Em _python_ existe um método da biblioteca re que permite obter somente palavras que se encontrem no inicio da 
frase, que correspondam às regras definidas, denominado _match()_.

Neste caso, como era pretendida a obtenção da palavra "hello" completa, nas suas diversas formas (ex.: "hello" e "Hello"), foi implementado o padrão **\b[Hh]ello\b**.

#### 1.2. Dada uma linha de texto, definir um programa que determina se a palavra "hello" aparece em qualquer posição da linha.
À semelhança do que acontece no exercício anterior, foi utilizado um método da biblioteca re, o _search()_, que permite procurar em toda a string um determinado padrão e devolve o mesmo, caso seja encontrado. Para esta procura, foi utilizado o mesmo padrão da questão anterior.

#### 1.3. Dada uma linha de texto, definir um programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha, admitindo que a palavra seja escrita com maiúsculas ou minúsculas.
Neste caso, o método utilizado foi o _findall()_, que permite obter todas as ocorrências de um determinado padrão ao longo da frase. Era necessário ter, ainda, em conta uma questão nova, a dimensão das letras, minúsculas ou maiúsculas. De modo a garantir que o tamanho das letras da palavra não influenciavam o output do programa, foi inserido o padrão **\b[hH][eE][lL][lL][oO]\b**, permitindo que em cada uma das letras fossem consideradas letras maiúsculas e minúsculas.

#### 1.4. Dada uma linha de texto, definir um programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha, substituindo cada uma por "*YEP*".
Para a resolução deste exercício, foi utilizado o método _sub()_, a partir do qual se pode substituir um determinado padrão, neste caso " " por uma expressão definida ("YEP"). 

Mais uma vez, foi considerado importante ter em conta a dimensão das letras, porém o modo de aplicação desta verificação difere da anterior. Para garantir que o tamanho das letras não afeta o desempenho do programa, foi associada, dentro do método, a _flag_ **re.IGNORECASE**.

#### 1.5. Dada uma linha de texto, definir um programa que pesquisa por todas as ocorrências do caracter vírgula, separando cada parte da linha por esse caracter.

De modo a resolver este exercício, foi implementado o método _split()_, a partir do qual é possível dividir a string a partir de um determinado padrão. Assim, foi aplicado este método ao padrão ",", originando uma lista composta pelos excertos da _string_ até ser detetado o padrão referido.

#### 2. Definir a função palavra_magica que recebe uma frase e determinar se a mesma termina com a expressão "por favor", seguida de um sinal válido de pontuação.
Para responder a este enunciado, foi necessário definir inicialmente os sinais de pontuação a considerar, de modo a permitir transparência e facilitar a implementação do porgrama. Assim, foram considerados os sinais que terminam frases, como **.** , **!** , **?** e **...** .

Após este processo de decisão, foi aplicado ao método _search()_ o padrão **por favor[\!\.\?]$|por favor\.{3}$**, procurando verificar somente no final das frases se existiria um "por favor", naturalmente seguido de um dos sinais de pontuação considerados. Este método foi selecionado, por ser necessária a obtenção de uma só ocorrência, pois se trata do final de uma frase.

#### 3. Define a função narcissismo que calcula quantas vezes a palavra "eu" aparece numa string.
De modo a desenvolver esta função, seria necessário encontrar todas as ocorrências da palavra "eu", nas suas variadas formas (ex.: EU, eu, Eu, etc). Para tal, foi efetuada a procura de todas estas ocorrências através do método _findall()_ para o padrão **\beu\b**, recorrendo à _flag_ re.IGNORECASE, a partir do qual se obtém uma lista com as mesmas.

Uma vez obtida esta lista, considera-se o número de ocorrências igual ao tamanho da lista, obtendo-se, assim, o que era pretendido.

#### 4. Define a função troca_de_curso que substitui todas as ocorrências de "LEI" numa linha pelo nome do curso dado à função.
Tendo em conta que para este exercício seria somente necessário substituir todas as ocorrências de um padrão definido por um nome fornecido à função, recorreu-se ao método _sub()_, atuando sobre o padrão **LEI**.

#### 5. Define a função soma_string que recebe uma string com vários números separados por uma vírgula (e.g., "1,2,3,4,5") e devolve a soma destes números.
Nesta função, foi aplicado o método _split()_ para dividir todos os valores dados numa _string_ e inseri-los numa lista, de modo a poder ser efetuada a soma entre estes num ciclo _for_, obtendo-se o valor total.

#### 6. Define a função pronomes que encontra e devolve todos os pronomes pessoais presentes numa frase, i.e., "eu", "tu", "ele", "ela", etc., com atenção para letras maiúsculas ou minúsculas.
De modo a resolver este enunciado, foi aplicado o método _findall()_ ao grupo de pronomes pessoais existentes 
(**(eu|tu|ele|ela|nós|vós|eles|elas|mim|ti|si|ele|ela|nos|vos|se|eles|elas**), garantindo através da inserção de **\b** no início e no final da espressão acima que estas eram palavras completas e não componentes de outras palavras, o que poderia proporcionar resultados incorretos, por exemplo, o "se" que na língua portuguêsa ocorre recorrentemente inserido em palavras como "fosse", "sente", etc.

Adicionalmente, foi ainda inserida a _flag_ referida em enunciados anteriores re.IGNORECASE, pelo mesmo motivo dos casos anteriores.

#### 7. Define a função variavel_valida que recebe uma string e determina se a mesma é um nome válido para uma variável, ou seja, se começa por uma letra e apenas contém letras, números ou underscores.
Visto que estamos somente a analisar uma variável, a procura no início da frase seria suficiente, daí o uso do método _match()_. 

Era pretendida a averiguação da validade da variável. Assim, foi estabelecido o padrão **[a-zA-Z]+[a-zA-Z\d_]*$**,
no qual a variável tem de se iniciar por uma letra, maiúscula ou minúscula, [a-zA-Z], e poderá conter letras (a-zA-Z), números (\d) ou _underscores_ (_), na quantidade pretendida (*) (zero ou múltiplas vezes), terminando somente com este tipo de caracteres ($).

#### 8. Define a função inteiros que devolve todos os números inteiros presentes numa string. Um número inteiro pode conter um ou mais dígitos e pode ser positivo ou negativo.
Nesta situação, dada a necessidade de obter todos os números inteiros de uma _string_, utilizou-se o método _findall()_ associado ao padrão **[^,]\b[-+]?\d+\b[^,]**. Este padrão permite estabelecer que a procura deve ser efetuada por um ou mais valores (\d+), que não estejam inseridos no interior de alguma palavra (\b), podendo ter ou não um + ou um -, como representação de este ser positivo ou negativo.

#### 9. Define a função underscores que substitui todos os espaços numa string por underscores. Se aparecerem vários espaços seguidos, devem ser substituídos por apenas um underscore.
A substituição de espaços numa _string_ por um _underscore_ é facilmente efetuada recorrendo ao método _sub()_, no qual se fornece o padrão " " e o caracter pelo qual se pretende substituir. Porém, o desafio residia na substituição de múltiplos espaços consecutivos por um só _underscore_, o que fica resolvido acrescentando o sinal + após o espaço no padrão definido (**" +"**), indicando que poderá ser considerado um ou múltiplos espaços para uma só substituição.

#### 10. Define a função codigos_postais que recebe uma lista de códigos postais válidos e divide-os com base no hífen. A função deve devolver uma lista de pares.
Considerando que o objetivo deste enunciado era obter uma lista de pares correspondentes às duas partes de cada código postal, foi necessário percorrer a lista inicial de códigos postais no formato normal e aplicar o método _split()_ pelo caracter "**-**". Aquando desta separação, cada parte de cada código postal foi inserida num tuplo (escolha pessoal para armazenar a informação), que por sua vez era inserido na lista final.

### Desafios
- Conseguir obter somente os números inteiros, sem retirar somente a vírgula
- Garantir todas as condições de verificação de escrita