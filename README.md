##GYM_BRO_API

Este repositorio trata sobre a api da aplicacao Gym Bro.

Para utiliza-la corretamente, siga o passo a passo abixo, de modo que ao final tera acesso as respectivas rotas.

Criando o ambiente virtual python

- virtualenv venv
- source venv/bin/activate

Instalacao de dependencias via pip

- pip install -r requirements.txt

Para rodar a aplicacao basta das o comando

- flask run

Para debugar o programa basta dar o comando

- flask --debug run

Para acessar o swagger:

- http://localhost:5000/docs

A rota da api e:

- http://localhost:5000

###SWAGGER

Existem 4 rotas no swagger, a de login('/login'), a de registro('/register'), a de listar todos os exercicios cadastrados('/exercise->get') e a de cadastrar novo exercicio('/exercise->post').

- ROTAS POST E GET DOS EXERCISES

As rotas de login e registro sao livres, ou seja, nao precisam de token de acesso para serem chamadas, ja as outras duas precisam, entao caso queira ver o funcionamento das ultimas, sugiro fazer o login no proprio swagger, copiar o token de acesso, clicar em authorize na tela do swagger, digitar o texto Bearer e colar o token em seguida com um espaco, desta maneira poderam ser feitas as chamadas para as outras rotas fechadas.
