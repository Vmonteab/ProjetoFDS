# ProjetoFDS
- Esse repositório contém a criação do Front-End e do Back-End do nosso projeto.

# Objetivo do Projeto
- O nosso projeto visa facilitar, por meio da criação de uma plataforma digital, a organização e a distribuição dos notebooks e livros da Cesar School para os seus alunos.

# Linguagens de Programação
- Python, HTML, CSS

# Instalação
- pip install -r requirements.txt

# Link do Jira
- https://vmonteab.atlassian.net/jira/software/projects/FDS/boards/1

# Utilização

Instalar o projeto usando o venv é recomendado, porém é possível instalar sem usá-lo também.

Ative o virtualenv no projeto:

    $ virtualenv project-env
    $ source project-env/bin/activate
    
Caso não tenha o django instalado ainda execute:

    $ pip3 install django
    
# Começando

Primeiramente clone esse repositório do Github e entre em seu diretório:

    $ git clone https://github.com/theomilll/ProjetoFDS.git
    $ cd ProjetoFDS

Instale os requirements:

    $ pip install requirements.txt
    
Aplique as migrações do banco de dados:
 
    $ python manage.py migrate
    
Agora, basta apenas rodar o servidor localmente:

    $ python manage.py runserver
    

# Issues/bugs

 Bugs
- Na aplicação do Heroku, quando um livro/computador é reservado, ele muda de posição. Esse Bug só ocorre na aplicação do Heroku, e não quando o código é rodado de maneira local.

# Heroku
- Login: theo
- Senha: fdsprojeto
- https://reservacesarr.herokuapp.com/

# Integrantes do Grupo
- Bernardo Meneses -- bmn@cesar.school

- Lara Pessoa -- lpn@cesar.school

- Leonardo Medeiros de Freitas -- lmf@cesar.school

- Raul Luiz Correia do Monte -- rlcm@cesar.school

- Théo Moura -- tam4@cesar.school

- Victor Montenegro -- vmab@cesar.school

- Vinícius Gonçalves -- vgp@cesar.school


