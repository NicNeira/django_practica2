from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from store.models import Product, CustomUser

# --- CRUD para Productos ---

def admin_products(request):
    if not request.session.get('user_id'):
        return redirect('login')
    
    user = get_object_or_404(CustomUser, id=request.session['user_id'])
    if not user.is_admin:
        messages.error(request, 'No tienes permisos para acceder a esta página.')
        return redirect('index')
    
    products = Product.objects.all()
    return render(request, 'administration/product_list.html', {'products': products})

def create_product(request):
    if not request.session.get('user_id') or not CustomUser.objects.get(id=request.session['user_id']).is_admin:
        return redirect('login')
    
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']
        
        product = Product(name=name, description=description, price=price, image=image)
        product.save()
        messages.success(request, 'Producto creado exitosamente.')
        return redirect('admin_products')
    
    return render(request, 'administration/product_create.html')

def update_product(request, product_id):
    if not request.session.get('user_id') or not CustomUser.objects.get(id=request.session['user_id']).is_admin:
        return redirect('login')
    
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        messages.success(request, 'Producto actualizado exitosamente.')
        return redirect('admin_products')
    
    return render(request, 'administration/product_update.html', {'product': product})

def delete_product(request, product_id):
    if not request.session.get('user_id') or not CustomUser.objects.get(id=request.session['user_id']).is_admin:
        return redirect('login')
    
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Producto eliminado exitosamente.')
    return redirect('admin_products')

# --- CRUD para Usuarios ---

def admin_users(request):
    if not request.session.get('user_id'):
        return redirect('login')
    
    user = get_object_or_404(CustomUser, id=request.session['user_id'])
    if not user.is_admin:
        messages.error(request, 'No tienes permisos para acceder a esta página.')
        return redirect('index')
    
    users = CustomUser.objects.all()
    return render(request, 'administration/user_list.html', {'users': users})

def create_user(request):
    if not request.session.get('user_id') or not CustomUser.objects.get(id=request.session['user_id']).is_admin:
        return redirect('login')
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        is_admin = 'is_admin' in request.POST
        
        # En un escenario real, deberíamos hashear la contraseña
        # from django.contrib.auth.hashers import make_password
        # hashed_password = make_password(password)
        
        user = CustomUser(username=username, email=email, password=password, is_admin=is_admin)
        user.save()
        messages.success(request, 'Usuario creado exitosamente.')
        return redirect('admin_users')
    
    return render(request, 'administration/user_create.html')

def update_user(request, user_id):
    if not request.session.get('user_id') or not CustomUser.objects.get(id=request.session['user_id']).is_admin:
        return redirect('login')
    
    user = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        if request.POST['password']:
            # Actualiza la contraseña solo si se proporciona una nueva
            user.password = request.POST['password']  # Recuerda hashear en un escenario real
        user.is_admin = 'is_admin' in request.POST
        user.save()
        messages.success(request, 'Usuario actualizado exitosamente.')
        return redirect('admin_users')
    
    return render(request, 'administration/user_update.html', {'user': user})

def delete_user(request, user_id):
    if not request.session.get('user_id') or not CustomUser.objects.get(id=request.session['user_id']).is_admin:
        return redirect('login')
    
    user = get_object_or_404(CustomUser, id=user_id)
    if user.id == request.session['user_id']:
        messages.error(request, 'No puedes eliminar tu propio usuario.')
        return redirect('admin_users')
    
    user.delete()
    messages.success(request, 'Usuario eliminado exitosamente.')
    return redirect('admin_users')