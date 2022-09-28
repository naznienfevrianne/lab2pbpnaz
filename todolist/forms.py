from django.forms import ModelForm
from django import forms
from todolist.models import TaskToDoList
import datetime
from django.utils.timezone import now
class TaskForm(ModelForm):
    title  = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    date = datetime.date.today()

    class Meta:
        model = TaskToDoList
        fields = ['title', 'description']
