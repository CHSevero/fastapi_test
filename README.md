# Desafio
Desenvolva uma API com a biblioteca FastAPI, com os seguintes requisitos:

1. Autenticação com OAuth2, protegendo todas as rotas, gerando token, que expira a cada hora, e o token deve ser utilizado em todos os endpoints;
2. Desenvolva um endpoint com request method POST, com payload: User (Str), Order (Float), PreviousOrder (Boolean), retornando um JSON com a RESPONSE 200 e os items do payload. Lembrando que esse item deve seguir as regras do item 01;
3. Desenvolva um endpoint com request method GET, buscando dados da API OpenBreweries (https://api.openbrewerydb.org/breweries/), mostrando no resultado apenas um dicionário com os nomes das cervejas que estarão em uma lista.
4. Entrega: github público ou zip com o seu nome. Data limite: 01 de Dezembro as 09:00.

## Requisitos
Foi utilizado um ambiente linux/debain para o desenvolvimento.
1. Python3.9.6
2. Aconselho criar um ambiente virtual:
   1. ```python3.9 -m pip install virtualenv```
   2. ```python3.9 -m virtualenv env```
   3. ```source env/bin/activate```
3. Instalação dos requisitos:
   ```pip install -r requirements.txt```

## Execução
1. run: ```uvicorn main:app --reload```
2. Api docs: http://127.0.0.1:8000/docs#
3. Autenticação:
   1. username: ``johndoe``
   2. password: ``1a6c75e61de6b04fe76788ce0febe04781e01ce87564371739afba8877e09546``