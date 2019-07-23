# Easy Login Demo

This is a demo project of integration Django project with [Easy Login library](https://github.com/SoftServeInc/django-easy-login).

## Demo site

**Demo** available on: https://django-easy-login.herokuapp.com/


### Requirements

Python (3.5, 3.6, 3.7)
Django (11.1)

### Installation

- To install Easy Login library
```python
under construction
```

- To install Demo project

```git
git clone https://github.com/yuriiZherebukh/easy_login_demo
```

- Configure your [Heroku](https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html) account for Django application

- Declare variables from `easy_login_demo/settings.py` required for running on Heroku server
```python
SECRET_KEY = "Some Secret key"
DEBUG = True
EASY_URL_REDIRECT = r"path_to_easy_login_app"
DATABASES = "PostgreSQL_URL_to_Heroku_server"
``` 
- Publish Demo project on Heroku App and start it
