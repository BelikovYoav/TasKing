from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Task(models.Model):
    assignee = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='assign', blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    points = models.IntegerField(validators=[MaxValueValidator(10)])
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Task {self.title}'

    def approve(self):
        self.approved = True
        self.save()

    def dis_approve(self):
        self.approved = False
        self.save()
