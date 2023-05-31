from django.db import models


class Todo(models.Model):
    task_name = models.CharField(max_length=250)
    task_description = models.TextField()
    task_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    task_status = models.BooleanField()

    def __str__(self):
        return self.task_name