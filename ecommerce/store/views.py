from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product, CustomUser

def index(request):
    return render(request, 'store/index.html')

def about(request):
    return render(request, 'store/about.html')

def products(request):
    products = Product.objects.all()[:10]
    return render(request, 'store/products.html', {'products': products})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = CustomUser.objects.filter(username=username, password=password).first()
        if user and user.is_admin:
            request.session['user_id'] = user.id
            return redirect('index')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'store/login.html')

def logout_view(request):
    del request.session['user_id']
    return redirect('index')