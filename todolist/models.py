from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import now
# Create your models here.

class TaskToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True);
    date = models.DateField(default=datetime.date.today())
    title = models.CharField(max_length=100)
    description = models.TextField();

    def __str__(self):
        return self.title