# Django Rest Api

This a little test for my Django skill and to try Docker. 

## Installation

First Install python 3.11
Linux:
Install pyenv (if you haven't already)
```bash
curl https://pyenv.run | bash
```

### Install Python 3.11

Linux:
```bash
pyenv install 3.11.0
```

Windows:
```bash
choco install python --version=3.11.0
```


Clone the project with this command
```bash
git clone https://github.com/antros024/Test_Django_API.git
```

Go in the repository
### Command to install

Commande to install what you need to run the project
```bash
pip install -r requirements.txt
```

Command to see check change from your models.py
```bash
python manage.py makemigrations articles
```

To create the table in your database
```bash
python manage.py sqlmigrate articles 0001
```

Apply changes
```bash
python manage.py migrate
```

To run the Django server
```bash
python manage.py runserver
```

To run the test from tests.py
```bash
python manage.py test
```

## Install Docker
Install Docker
[Download Link](https://www.docker.com/get-started/)

Build your container
```bash
docker build -t my_django_app . 
```

To run your Docker
```bash
docker run -p 8000:8000 my_django_app  
```