# Todo List

In the Todo App, we need a title, where we specify what to do.
The description will elaborate task. Then on which date we want that task to be completed.
And finally, we have a boolean field that will tell us whether the task is completed or not.

# REQUIREMENTS
python version 3.10


## Apis

- GET /todos/ - get the list of all todo
- POST /task/todos/ -> Create new todo
- GET /todos/<id> - get the detail of a particular id
- PUT /todos/<id> - update the todo
- DELETE /todos/<id> - delete the todo


# ADMIN LOGIN DETAILS
username-- admin, password-- superuser

## HOW TO RUN
1. `pip install -r requirements.txt` to install the dependencies of this project
2.  `python manage.py runserver`
after install requirement.txt to run the server use above command
3. visit this url to see todo list `http://127.0.0.1:8000/task/todos`
4. visit `http://127.0.0.1:8000/admin/ to use admin panel`

# RUN VIA DOCKER
1. do docker build `docker build .`
2. run `docker images`
3. copy image id and run `docker run -p 80:8000 (image's id)`