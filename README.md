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

```zsh
virtualenv gplays-env
```

```zsh
source gplays-env/bin/activate
```

```zsh
pip install django 
pip install djangorestframework
```

```zsh
# WSL2
django-admin startproject gplaysbackend .

# Windows
python manage.py startproject gplaysbackend .

# Já feito! Não é necessário repetir!
```

```zsh
# WSL2
django-admin startapp gplaysapi .

# Windows
python manage.py startapp gplaysapi .

# Já feito! Não é necessário repetir!
```

```zsh
cd gplays-backend
python manage.py runserver
```