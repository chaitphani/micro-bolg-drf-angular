## Requirements

You need the following to run this app:

* Python 3.5 or higher (Python 2.x is not supported by Django 2.x)
* [Pipenv](https://pipenv.readthedocs.io/)
* Node v8.x or higher
* NPM v5.x or higher

## Setup

Open a terminal at the repo root, and run the following:

```bash
python -m venv venv
pip install -r requirements.txt
cd microblog/front-end
npm install
ng build
cd ../..
python manage.py runserver
```

Your app will be available at http://127.0.0.1:8000.

## Database

This project uses a SQLite database, which lives in the file `db.sqlite3`. SQLite3 support should be available out of the box on most modern operating systems. 

## Logging into the app

The database included in this repository contains two users. The following are their usernames and passwords, which you may use for testing:

- chaitu / 12345
- phani / 12345

NOTE: can able to create post after successful login.

## creating users if required:

Head over to localhost:8000/api/users endpoint(use either browser or postman to insert data).
