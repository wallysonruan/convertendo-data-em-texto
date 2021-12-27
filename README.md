<h1>pythonRandomCodes</h1>
<details>
<summary>"date2text": Conversor de DATA para TEXTO</summary>
<br>
<time datetime="2021-12-22"><p>Escrevi esse conversor porque um amigo (Felipe) recebeu, na faculdade, a tarefa de escrever um conversor de data de aniversário para texto, comentou comigo e decidi tentar resolver. Comecei a escrever e achei interessante a ideia, fui além e escrevi um conversor de datas que não se prende a data alguma e sim a tipos, ou seja, mesmo nos anos 3k, 5k, ... o conversor irá funcionar.</p>
<time datetime="2021-12-27"><p>Esse conversor me tomou bastante tempo porque eu o refatorei várias vezes e a cada refatoração eu aprendia algo novo e logo implementava. A primeira versão funcional é a 4, pois as outras eu refatorei e/ou mudei totalmente a lógica do código.</p>
  <h2>Meta Inicial:</h2>
  <ul>
    <li>Receber uma data numérica, dia e mês, e devolver ela em formato de texto ("por extenso"). <time datetime="2021-12-22">(CONCLUÍDA)</time></li>
  </ul>
  <h2>Metas Atuais:</h2>
  <ul>
  <time datetime="2021-12-23">
    <li>Receber uma data numérica, dia, mês e ano, e devolver ela em formato de texto ("por extenso"). (CONCLUÍDA)</li>
    <li>Condicionar, com uma regEx e um laço de repetição, o input do usuário. (CONCLUÍDA)</li>
    <li>Laço de repetição para que o usuário possa converter outras datas sem que o programa encerre. (CONCLUÍDA)</li>
    <li>Adicionar possibilidade de ter a data retornada dentro de um texto definido pelo usuário, usando a lógica de TAG.</li>
    <li>Opção de idioma.</li>
    <li>Opção de formato de data.</li>
   </time>
    <time datetime="2021-12-27">
    <li>Adicionar GUI.</li>
    <li>Aceitar anos constituídos apenas de unidades, dezenas ou centenas.</li>
    <li>Aceitar "anos negativos", isto é, anos anteriores a Cristo (delimitador atual).</li>
  </ul>
 <h3>Aprendizado:</h3>
  <ul>
    <li>Aprendi a estrutura de dados "dicionario", similar ao objeto do Javascript, e como acessá-la (tanto dicionários simples, quanto os múltiplos).</li>
    <li>A escrever expressões regulares, o que me levou a aprender e usar a biblioteca nativa "re", e as usar para validar input do usuário.</li>
    <li>Conheci e usei a biblioteca nativa datetime.</li>
    <li>Pratiquei o uso das estruturas: if/else e try/exception aninhadas, seja intercalando elas ou aninhando apenas as de mesmo tipo.</li>
    <li>Graças às dicas do IDE Pycharm, pude aprimorar meu uso da estrutura IF/ELSE aliada a valores booleanos. Anteriormente, eu estava a escrever:<code>if x == True: {do this}</code> e <code>if x == False: {do this}</code>, depois das dicas do IDE estou a escrever: <code>if x:{do this}</code> e <code>if not x: {do this}</code>.</li>
  </ul>
</details>
