from fabric.api import local


def migrations():
    local('python3 documents_tracer/manage.py makemigrations id_cards')
    local('python3 documents_tracer/manage.py migrate')


def runserver():
    local('python3 documents_tracer/manage.py runserver 7000')
