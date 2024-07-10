import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product, CustomUser
from django.shortcuts import render
from datetime import datetime
from .forms import ContactForm

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

def consultar_api(request):
    api_key = '9TB3Hax6IdLA0e9kHlMhADXF4viuQcoO'
    location_url = f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q=SANTIAGO'
    location_response = requests.get(location_url).json()
    location_key = location_response[0]['Key']  # Obtener el LocationKey de la respuesta
    
    weather_url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}'
    weather_response = requests.get(weather_url).json()
    temperature = weather_response[0]['Temperature']['Metric']['Value']  # Obtener la temperatura
    observation_time = weather_response[0]['LocalObservationDateTime']

    # Formatear la fecha
    formatted_date = datetime.fromisoformat(observation_time).strftime('%d-%m-%Y %H:%M:%S')

    print(f'La Fecha es {formatted_date}°C')

    context = {
        'location_key': location_key,
        'temperature': temperature,
        'location_city': location_response[0]['LocalizedName'],
        'location_country': location_response[0]['Country']['LocalizedName'],
        'formatted_date': formatted_date,
        'Link': weather_response[0]['Link'],
    }

    return render(request, 'consultar_api.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')