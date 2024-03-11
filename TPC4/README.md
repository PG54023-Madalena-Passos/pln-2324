## Trabalho de casa 4

Neste projeto era pretendido o desenvolvimento de uma página html, na qual fossem apresentados os meus _hobbies_. Após alguma ponderação, optei por um formato idêntico ao de currículo, incluindo uma secção de introdução, seguido dos _hobbies_, de modo a garantir alguma estruturação.

### Estrutura do Código
Este ficheiro encontra-se dividido em duas partes, uma relativa à estilização da página, recorrendo a _css_, e outra referente ao conteúdo desta, usando _html_.

Considerando o conteúdo da página, este encontra-se repartido por secções, permitindo uma melhor compreensão do mesmo.

#### Secções

- _Header_ / Cabeçalho;
- Introdução;
- _Hobbies_
  * Neurociência;
  * Ver séries e filmes;
  * Ler;
  * Ouvir Música;
  * Projetos;
- _Footer_ / Rodapé;

#### Estrutura HTML
A parte _html_ da página, inserida no _body_ do mesmo, é composta por:

- uma **barra de navegação**, na qual são estabelecidas **ligações a cada secção da página**, de modo a facilitar o acesso a estas. Neste contexto em específico poderá não fazer tanto sentido, dada a pequena extensão da página, porém numa perspetiva de expansão é útil a sua presença;

<figure style="text-align: center;">
  <img src="pagina_html\nav.png" alt="Barra_de_navegação">
  <figcaption style="font-size: smaller; color: darkgray;">Figura 1. Barra de Navegação.</figcaption>
</figure>

- um **_container_ relativo à introdução**, contendo uma **imagem** ajustada e com ligação ao ficheiro contendo o meu _curriculum vitae_, um **texto** "Sobre mim" e um **botão** remetendo, à semelhança da barra de navegação, para o conteúdo mais relevante, neste caso os _hobbies_ de modo geral;

<figure style="text-align: center;">
  <img src="pagina_html\introducao.png" alt="Introdução">
  <figcaption style="font-size: smaller; color: darkgray;">Figura 2. Introdução.</figcaption>
</figure>

- uma região principal (**\<main>**), contendo 5 secções, relativas aos meus _hobbies_, dentro das quais existe uma 
**grelha**, contendo em cada **_item_** uma **imagem à esquerda** e um **texto descritivo à direita**.

<figure style="text-align: center;">
  <img src="pagina_html\hobbies.png" alt="Secções">
  <figcaption style="font-size: smaller; color: darkgray;">Figura 3. Secções.</figcaption>
</figure>

**Nota:** As secções impares apresentam uma diferença clara das restantes, um **gradiente** progredindo de transparente 
para cinza e de novo para transparente como fundo.

#### Resultado Final

<figure style="text-align: center;">
  <img src="pagina_html\pagina_final.png" alt="Secções">
  <figcaption style="font-size: smaller; color: darkgray;">Figura 4. Resultado Final.</figcaption>
</figure>

### Desafios
- Tentativa de utilização de bibliotecas;
- Exploração inicial das funcionalidades existentes em _html_.