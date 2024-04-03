'''
# steps to build project

django-admin startproject DjangoRestApp .
python manage.py migrate
python manage.py createsuperuser

python manage.py startapp PeopleApp
python manage.py makemigrations PeopleApp
python manage.py migrate

python manage.py startapp ArtifactsApp
python manage.py makemigrations ArtifactsApp
python manage.py migrate

python manage.py startapp BooksApp
python manage.py makemigrations BooksApp
python manage.py migrate


python manage.py startapp VehiclesApp
python manage.py makemigrations VehiclesApp
python manage.py migrate

python manage.py runserver 127.0.0.1:80

curl -s http://127.0.0.1:80/api/artifacts/ | python -m json.tool
curl -s -X POST -d "name=post_new_item" -d "shiny=True" http://127.0.0.1:80/api/artifacts/
'''