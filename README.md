1. SETUP a virtual env
   `python3 -m venv [env_name]`
2.  start the virtual env
   `source [env_name]/bin/activate`
3. install django
   `pip3 install django`
4. check django is installed
   `python3 -m django version`
5. create a django project
   `django-admin startproject [project_name]`
6. run the server
   `python3 manage.py runserver`
7. create an app
   `python3 manage.py startapp [app_name]`
   or `python3 -m django startapp [app_name]`


8. open shell
   `python3 manage.py shell`
9. migrate 
    ```shell
    python3 manage.py makemigration
    python3 manage.py migrate
    ```