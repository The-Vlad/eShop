from django.contrib.auth import login as logindj, authenticate, logout
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView
from django.contrib.auth.models import User,Group
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
from .forms import *


# Create your views here.

def index(request):
    product_objects = Product.objects.order_by('name')
    # TODO: Добавить категории в товары и отобразить на страничке индекс, а также убрать панель с переходами на страницы
    return render(request, 'main/index.html', {'title': 'Главная страница', 'content': product_objects})


def login(request):
    form = LoginForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
    return render(request, "family/login.html",{"form":form})


def register(request):
    if request.method == 'POST':
        user_form = RegisterUser(request.POST)

        if  user_form.is_valid():
            user = User(email = user_form.cleaned_data["email"],
                                            first_name=user_form.cleaned_data["first_name"],
                                            last_name=user_form.cleaned_data["last_name"],
                                            username=user_form.cleaned_data['username'])
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            return HttpResponseRedirect("/")
        else:

            return HttpResponseRedirect("/register")
    else:
        user_form = RegisterUser()

    return render(request,"main/register.html",{"form":user_form})


def about(request):
    return render(request, 'main/about.html')


def search(request):
    return render(request, 'main/search.html')


def secret(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма некорректно заполнена'

    form = ProductForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/secret.html', context)


@require_POST
def checkusername(request):
    post = json.loads(request.body.decode("utf-8"))
    if User.objects.filter(username=post.get("username")).exists():
        return JsonResponse({"exists": True})
    return JsonResponse({"exists": False})


def cart(request):
    return render(request,'main/cart.html')