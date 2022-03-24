## Infra

* [Configuração Inicial do WSL2](https://fonti95.notion.site/Trabalho-linux-77bb89d5f7a342339e9818dc973275cd)

* [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04)

* [Creating a REST API using Django Rest Framework](https://www.ginkgobioworks.com/2021/02/04/creating-a-rest-api-using-django-rest-framework/)

* [Criando Uma API Rest Utilizando Django Rest Framework](https://medium.com/@marcosrabaioli/criando-uma-api-rest-utilizando-django-rest-framework-parte-1-55ac3e394fa)

```zsh
ssh -i .\gplays-ics_key.pem gplays@20.206.77.14
```
Dentro do diretório do repositório.
```zsh
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```
## Django

Por algum motivo, no WSL2, se tiver o modulo 'rest_framework' ele nao funciona.

OBS: Ja ajeitei eu sou burro.

```zsh
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
```
Instalar dependências para criar e gerenciar o projeto na vm.

```zsh
virtualenv gplays-env
```
Ao entrar no diretório do repositório, se não houver uma pasta chamada 'gplays-env' no diretório raiz, deve-se dar esse comando para criar o ambiente virtual Python.

```zsh
source gplays-env/bin/activate
```
Esse comando faz a conexão ao virtualenv do Python

```zsh
pip install django 
pip install djangorestframework
```
Esses passos devem ser dados ao conectar-se no virtual env, provavelmente aparecerá: (gplays-env) gplays@gplays-ics:~/gplays-ics/gplays-backend$ , assim você saberá que está conectado.

```zsh
# WSL2
django-admin startproject gplaysbackend .

# Windows
python manage.py startproject gplaysbackend .

# Já feito! Não é necessário repetir!
```
Esses passos servem para criar a base do projeto django, já está feito no repositório e não deve ser repetido.
OBS: Está dentro da pasta 'gplays-backend'

```zsh
# WSL2
django-admin startapp gplaysapi .

# Windows
python manage.py startapp gplaysapi .

# Já feito! Não é necessário repetir!
```
Esses passos servem para criar 0 projeto django em si, já está feito no repositório e não deve ser repetido.
OBS: Está dentro da pasta 'gplays-backend'

```zsh
cd gplays-backend
python3 manage.py runserver
```
Esses passos são para entrar na pasta do projeto django e rodar ele.

```zsh
manage.py makemigrations
manage.py migrate
```
Migration.