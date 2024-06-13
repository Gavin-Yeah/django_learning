1. SETUP a virtual env
   `python3 -m venv [env_name]`
2.  start the virtual env
   `source [env_name]/bin/activate`
3. install django
   `pip3 install django`
4. check django is installed
   `python3 -m django version`
or
5. insall django in a virtual env
   `pipenv install django`
   
6. activate virtual env
   `pipenv shell`



7. create a django project
   `django-admin startproject [project_name] .`
8. run the server
   `python3 manage.py runserver`
9.  create an app
   `python3 manage.py startapp [app_name]`
   or `python3 -m django startapp [app_name]`


8. open shell
   `python3 manage.py shell`
9. migrate 
    ```shell
    python3 manage.py makemigration
    python3 manage.py migrate
    ```
10. create a super user
    `python3 manage.py createsuperuser`

## add a template html
1. create a view function, return a render function
2. add path function in urls file
3.  add templates dir into template obj
 

## add static files
1. create a static folder in app folder
2. create a list named STATICFILES_DIRS
3. add static folder relative path 'myapp/static'
4. add {% load static %} at the beginning of the HTML file
5. use the image src="{% static 'img/dessert.jpg' %}"

## install django rest framework
1. pip3 install djangorestframework / pipenv install djangorestframework
2. add 'rest_framework' to INSTALLED_APPS list in settints.py in project folder
## install django debug toolbar
1. `pipenv install django-debug-toolbar`
2. add 'debug_toolbar' in settings.py
3. add  'debug_toolbar.middleware.DebugToolbarMiddleware' in MIDDLEWARE List
4. add INTERNAL_IPS = ["127.0.0.1"] in settings.py


## set renderer
1. add in settings.py
```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES':[
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}
```

## set up xml renderere
1. `pipenv install djangorestframework-xml`
2. add   'rest_framework_xml.renderers.XMLRenderer', in   'DEFAULT_RENDERER_CLASSES' list