from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


# Create your views here.

def index(request):
    product_objects = Product.objects.order_by('name')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'content': product_objects})


def login(request):
    return render(request, 'main/login.html')


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
