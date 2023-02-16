from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(null=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# In the Todo App, we need a title, where we specify what to do.
# The description will elaborate task. Then on which date we want that task to be completed.
# And finally, we have a boolean field that will tell us whether the task is completed or not.

