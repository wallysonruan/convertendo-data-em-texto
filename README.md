<h1>pythonRandomCodes</h1>
<details>
<summary>"numero2texto": Conversor de DATA para TEXTO</summary>
<br>
<time datetime="2021-12-22"><p>Escrevi esse conversor porque um amigo (Felipe) recebeu, na faculdade, a tarefa de escrever um conversor de data de aniversário para texto, comentou comigo e decidi tentar resolver. Comecei a escrever e achei interessante a ideia, fui além e escrevi um conversor de datas que não se prende a data alguma e sim a tipos, ou seja, mesmo nos anos 3k, 5k, ... o conversor irá funcionar.</p>
<p>Por conta desse pequeno projeto, usei pela primeira vez o tipo de dado DICIONARIO em Python e a biblioteca nativa DATETIME, além de estruturas condicionais com várias outras dentro.</p></time>
<br>
<h2>Meta Inicial:</h2>
  <ul>
    <li>Receber uma data numérica, dia e mês, e devolver ela em formato de texto ("por extenso"). <time datetime="2021-12-22">(CONCLUÍDA)</time></li>
  </ul>
  <h2>Metas Atuais:</h2>
  <ul>
  <time datetime="2021-12-23">
    <li>Receber uma data numérica, dia, mês e ano, e devolver ela em formato de texto ("por extenso"). (CONCLUÍDA)</li>
    <li>Adicionar opção de sistema de datas, ex.: dd/mm/aaaa e mm/dd/aaaa.</li>
    <li>Condicionar, com uma regEx e um laço de repetição, o input do usuário.</li>
    <li>Laço de repetição para que o usuário possa converter outras datas sem que o programa encerre.</li>
    <li>Adicionar possibilidade de ter a data retornada dentro de um texto definido pelo usuário, usando a lógica de TAG.</li>
   </time>
  </ul>
<h3>Pendências:</h3>
  <ul>
    <li>Validação do ano para quando esse tiver apenas 2 caracteres.</li>
    <li>Validação de escrita, restringir o usuário a escrever apenas de acordo com os modelos a seguir:
      <ul>
      <li>/(\d{2})\/(\"/"{1})/(\m{2})\/(\a{2,4})/<br><p><em>Essa é a minha primeira tentativa de escrever uma regEx, com ela eu quero dizer: O formato permitido é: "dd(até 2 caracteres)'/'(um caractere)mm(até 2 caracteres)'/'(um caractere)aaaa(de 2 até 4 caracteres)", irei estudar mais sobre e em seguida condicionar a serem numéricos.</em></p></li>
      </ul>
    </li>
    <li>Laço de repetição para que o usuário possa escolher outra data sem precisar reiniciar o programa.</li>
  </ul>
</details>
<!---->
<details>
<summary>"date2text-v2": Conversor de DATA para TEXTO</summary>
<br>
<h2>Meta Inicial:</h2>
  <ul>
    <li>Receber uma data numérica, dia e mês, e devolver ela em formato de texto ("por extenso"). <time datetime="2021-12-22">(CONCLUÍDA)</time></li>
  </ul>
  <h2>Metas Atuais:</h2>
  <ul>
  <time datetime="2021-12-23">
    <li>Receber uma data numérica, dia, mês e ano, e devolver ela em formato de texto ("por extenso"). (CONCLUÍDA)</li>
    <li>Adicionar opção de sistema de datas, ex.: dd/mm/aaaa e mm/dd/aaaa.</li>
    <li>Condicionar, com uma regEx e um laço de repetição, o input do usuário. (CONCLUÍDA)</li>
    <li>Laço de repetição para que o usuário possa converter outras datas sem que o programa encerre.</li>
    <li>Adicionar possibilidade de ter a data retornada dentro de um texto definido pelo usuário, usando a lógica de TAG.</li>
   </time>
  </ul>
<h3>Pendências:</h3>
  <ul>
    <li>Laço de repetição para que o usuário possa escolher outra data sem precisar reiniciar o programa.</li>
    <li>Opção de idioma.</li>
    <li>Opção de formato de data.</li>
  </ul>
</details>
