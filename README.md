Step:

1) Enable the Env
-> command: venv/Scripts/Activate

3) Install Require Package
-> command: pip install -r requirements.txt

2) Create Database in Phpmyadmin
-> 'NAME': 'drcsystem',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '3306',

3) Run command 
-> python manage.py migrate 
-> python manage.py makemigartion 
-> python manage.py migrate

4) Run Server
-> python manage.py runserver