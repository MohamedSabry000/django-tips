# Django Tip
is the output of days from Course django

# install dependencies
```
############################################################
#----------------------------------------------------------#
#............ install django into a virtualenv ............#
#----------------------------------------------------------#
############################################################
```

* sudo apt install python3-pip
* sudo pip3 install virtualenv
* mkdir django_project
* cd django_project
* virtualenv env
* source env/bin/activate
* which pip3
* pip3 install django
 * django-admin --version  #4.0.4
* pip install pymysql
* django-admin startproject djproj

in file `Day */django_project/djproj/djproj/settings.py`
create your database in mysql
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djdb',
        'USER': 'root',
        'PASSWORD': '',
    }
}
```

11- deactivate
# Start Project
create user admin via command:
* python manage.py createsuperuser

* python manage.py runserver
