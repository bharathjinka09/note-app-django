# GetNote

## Features

- Google Keep's clone
- Note with CRUD
- Tags to organize note
- Search Notes
- Beautiful yet simple UI
- Notes are encrpyted & safe with us. ([django-cryptography](https://github.com/georgemarshall/django-cryptography))

### 📖 Install

```
$ git clone https://github.com/ycv005/getnote.git
$ cd getnote
$ pipenv install
$ pipenv shell

# Run Migrations
$ python manage.py migrate

# Create a Superuser:
$ python manage.py createsuperuser

# Confirm everything is working:
$ python manage.py runserver

# Load the site at http://127.0.0.1:8000
```

To Run the django Interactive interpreter (shell)- `python manage.py shell`</br></br>
Any changes to db/models, run following code</br>
```
python manage.py makemigrations
python manage.py migrate
```
</br></br>
Any changes to static files, we need to collect static files (as result your new files will be added to static folder)</br>
```
python manage.py collectstatic
```
</br></br>

### Deployment
Yet to be deployed