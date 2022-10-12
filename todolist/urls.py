from django import views
from django.urls import path
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import todolist_json
from todolist.views import add_task
from todolist.views import todolist_ajax
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('json/', todolist_json, name="json"),
    path('todolist_ajax/', todolist_ajax, name="ajax"),
    path('add_task/', add_task, name="add_task")
]