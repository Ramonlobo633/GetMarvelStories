<h1>Script em Python que consome dados de uma API da Marvel e gera um conjunto de dados em formato csv </h1>
Este projeto contém algumas variáveis com nomes de personagens da marvel e a partir disso, é possivel gerar um conjunto de dados com todas as histórias em que os personagens fazem parte.<br/>
<br/>


Documentação API Marvel:<br/>
https://developer.marvel.com/docs#



<h2>Ambiente de desenvolvimento</h2>
<div>
    <ul>
        <li>Python 3.9</li>
        <li>Visual Studio Code (Community Edition)</li>
        <li>Windows 10</li>
    </ul>
<div>

<h2>Guia de instalação</h2>
<div>
    <strong>Clonar o repositório</strong><br/><br/>
    
    $ git clone https://github.com/Ramonlobo633/GetMarvelStories.git <br/><br/>
    $ cd GetMarvelStories/src <br/><br/>
    
</div>    

<strong>Instalar dependências</strong><br/>
<div>    
    $ pip install  -r requirements.txt<br/><br/>
</div>

<strong>Rodar a aplicação</strong><br/>
<div>
    $ python main.py<br/><br/>
    Aguarde alguns segundos e acesse a pasta src/data<br/><br/>
 </div>   
 
 <h2>Detalhes do conjunto de dados esperado</h2>
<div>
    <ul>
        <li>Colunas</li>
          <ul>
             <li>Id</li>
               <ul>
                 <li>Identificador único da história</li>
               </ul>
             <li>title</li>
                <ul>
                   <li>Título da história</li>
               </ul>
             <li>description</li>
                 <ul>
                   <li>Descrição da história</li>
               </ul>
             <li>type</li>
                <ul>
                   <li>Tipo da história</li>
               </ul>
             <li>modified</li>
                <ul>
                   <li>Data e hora da ultima modificação da história</li>
               </ul>
             <li>characters</li>
               <ul>
                   <li>Personagens envolvidos na história</li>
               </ul>
         </ul>
        <li>Formato CSV</li>
        <li>3831 Linhas</li>
    </ul>
<div>


