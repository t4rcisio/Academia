# Backend for TP2 in software engineering 1

Follow the next steps for setup backend

## Create and start virtual machine

```bash
$python -m venv .
$source ./venv/Scripts/activate
```

## Install dependencies

```bash
$pip install -r requirements.txt
```

## Configure environment

- Create a copy of `.env.example` inside **Academia** folder
- Rename to `.env`
- Fill all variables

## Make migrations

```bash
$python manage.py migrate
```

## Start project

```bash
$python manage.py runserver
```
