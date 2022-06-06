from django.contrib.auth import login as logindj, authenticate, logout
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView
from django.contrib.auth.models import User,Group
from django.http import HttpResponse, JsonResponse
import json
from .models import Product
from .forms import ProductForm


# Create your views here.

def index(request):
    product_objects = Product.objects.order_by('name')
    # TODO: Добавить категории в товары и отобразить на страничке индекс, а также убрать панель с переходами на страницы
    return render(request, 'main/index.html', {'title': 'Главная страница', 'content': product_objects})


def login(request):
    if request.method == 'POST' and User.objects.filter(username=request.POST["username"]).exists():
        logout(request)
        usr = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usr is not None:
            logindj(request, usr)
            return redirect('home')
    return render(request, 'main/login.html')


def register(request):
    if request.method == 'POST' and not User.objects.filter(username=request.POST["username"]).exists():
        vertobussy = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
        vertobussy.save()
        logindj(request,vertobussy)
        return redirect('home')
    return render(request, 'main/register.html')


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