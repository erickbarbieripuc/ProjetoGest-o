## Como rodar o projeto Django (Windows PowerShell)

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
django-admin startproject gestao .
python manage.py startapp core
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
