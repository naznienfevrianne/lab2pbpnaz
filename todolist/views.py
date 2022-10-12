from django.shortcuts import render
# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from todolist.models import TaskToDoList
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
from .forms import TaskForm
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/todolist/login')
def show_todolist(request):
    data_task_todolist = TaskToDoList.objects.filter(user=request.user);
    context = {
        'list_task': data_task_todolist,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def todolist_json(request):
    list_task = TaskToDoList.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", list_task), content_type="application/json")

@login_required(login_url='/todolist/login/')
def todolist_ajax(request): 
    context = {
    'nama': 'Shafa',
    'last_login': request.COOKIES['last_login'],
}
    return render(request, 'todolist_ajax.html', context)

@login_required(login_url="/wishlist/login/")
@csrf_exempt
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        new_task = TaskToDoList.objects.create(
            title=title, 
            description=description, 
            date=datetime.datetime.now(),
            user=request.user, 
        )

        new_task.save()
        return HttpResponse("")
    return render(request, "create_task.html")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun telah berhasil dibuat!")
            return redirect('todolist:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            TaskToDoList.objects.create(title=title, description=description, date=datetime.date.today(), user=request.user)
            return redirect('todolist:show_todolist')
    else:
        form = TaskForm()

    context = {'form': form,
                "username": request.user.username}
    return render(request, 'create_task.html', context)