from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .serializer import TodoSerializer

# Create your views here.


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Here we used ModelViewSet. It was developed as a shortcut for common uses pattern.
#  Using ModelViewSet we can get List of all Todolist and also Create, Update, Delete.
# Now add the following code in the urls.py file inside the main folder.
