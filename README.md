![yamdb_workflow](https://github.com/reztsovdimitrii/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)
## Учебный проект 16 спринта. CI/CD для проекта API YAMDB.

### Cтек технологий:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=008080)](https://jwt.io/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=008080)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=008080)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/products/docker-hub)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=56C0C0&color=008080)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=56C0C0&color=008080)](https://cloud.yandex.ru/)

### Запуск проекта:

**Клонировать репозиторий и перейти в него в командной строке:**

`git clone https://github.com/reztsovdimitrii/yamdb_final.git`
`cd yamdb_final/`

**Cоздать и активировать виртуальное окружение:**

`python3 -m venv env`
`source env/bin/activate`
`python3 -m pip install --upgrade pip`

**Установить зависимости из файла requirements.txt:**

`pip install -r api_yamdb/requirements.txt`

**Запустить приложение в контейнерах:**

из директории infra/

`docker-compose up -d --build`

**Выполнить миграции:**

из директории infra/

`docker-compose exec web python manage.py migrate`

**Создать суперпользователя:**

из директории infra/

`docker-compose exec web python manage.py createsuperuser`

**Собрать статику:**

из директории infra/

`docker-compose exec web python manage.py collectstatic --no-input`

**Остановить приложение в контейнерах:**

из директории infra/

`docker-compose down -v`

**Запуск pytest:**

при запущенном виртуальном окружении

`cd yamdb_final && pytest`

**Документация API с примерами:**
/redoc/  
шаблон наполнения env-файла  
см.  
infra/.env.template  
описание команды для заполнения базы данными  
`cd api_yamdb && python manage.py loaddata ../infra/fixtures.json`  

### Автор:
Резцов Дмитрий [reztsovdimitrii](https://github.com/reztsovdimitrii)

### Примеры запросов:
http://51.250.102.111/redoc/
http://51.250.102.111/admin/
http://51.250.102.111/api/v1/