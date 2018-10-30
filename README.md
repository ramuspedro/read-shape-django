# Read shape django

### Creating the project

```
docker-compose run backend django-admin.py startproject project .

sudo chown -R $USER .
```

### Run the project first time

```
docker-compose run frontend npm install
```

### Run the project everyday

```
docker-compose up
```

### Problems

* Delete migration of an APP

```
# enter on app folder and run:

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```