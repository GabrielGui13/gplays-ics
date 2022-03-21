## Infra

* [Configuração Inicial do WSL2](https://fonti95.notion.site/Trabalho-linux-77bb89d5f7a342339e9818dc973275cd)

* [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04)

* [Creating a REST API using Django Rest Framework](https://www.ginkgobioworks.com/2021/02/04/creating-a-rest-api-using-django-rest-framework/)

```zsh
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```
## Django

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
django-admin startproject gplaysbackend .
# Já feito! Não é necessário repetir!
```

