from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product, CustomUser

def index(request):
    is_admin = request.session.get('is_admin', False)
    return render(request, 'store/index.html', {'is_admin': is_admin})

def about(request):
    is_admin = request.session.get('is_admin', False)
    return render(request, 'store/about.html', {'is_admin': is_admin})

def products(request):
    products = Product.objects.all()[:10]
    is_admin = request.session.get('is_admin', False)
    return render(request, 'store/products.html', {'products': products, 'is_admin': is_admin})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = CustomUser.objects.filter(username=username, password=password).first()
        if user and user.is_admin:
            request.session['user_id'] = user.id
            request.session['is_admin'] = True
            return redirect('index')
        elif user:
            request.session['user_id'] = user.id
            request.session['is_admin'] = False
            return redirect('index')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'store/login.html')

def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'is_admin' in request.session:
        del request.session['is_admin']
    return redirect('index')
