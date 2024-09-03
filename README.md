# django_wait_for_db
 Django app that provides a simple command to wait for the database to be ready before starting the server.

## Usage

Add `django_wait_for_db` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'wait_for_db',
    ...
]
```

Then run the following command:

```bash
python manage.py wait_for_db
```

This will wait for the database to be ready before starting the server.
This is useful when you are using Docker and you want to start the Django server before the database is ready or when you are in an environment where the database is not always available when the Django server starts.

Exemple of a Dockerfile:

```Dockerfile
FROM python:3.8

(.......)

CMD python manage.py wait_for_db \
    && python manage.py runserver
```
