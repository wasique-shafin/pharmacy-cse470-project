# pharmacy-cse470-project
---
## About Project
- **Models** are in `MVC/models.py`
- **Controllers** are in `MVC/controllers.py`
- **Views** are in `MVC/views/*`
- **Routes** are in `MVC/routes.py`

## Before Running
### Installation
- `python`
- `python-virtualenv`
    - Or `$ pip install django pillow`
### Build Python Virtual Environment (build once only)
- `$ python -m venv env`
- `$ source env/bin/activate` for **Linux/MacOS**
- `$ env\Scripts\activate.bat` for **Windows**
- `$ pip install django pillow`

## Run Project
### Activate Python Virtual Environment
- `$ source env/bin/activate` for **Linux/MacOS**
- `$ env\Scripts\activate.bat` for **Windows**
### Start Project Server
- `$ python manage.py runserver`
### Access Project Website
- Open `http://127.0.0.1:8000/` in **Browser**
