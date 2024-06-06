# Djanjo

### Paso 2: Crear un entorno virtual y un proyecto Django

**En general trabajo desde VScode y con una terminal de powershell**

1. **Crear un entorno virtual:**
    
    ```
    python -m venv myenv
    ```
    
2. **Activar el entorno virtual:**
    - En macOS/Linux:
        
        ```
        source myenv/bin/activate
        ```
        
    - En Windows:
        
        ```
        myenv\Scripts\activate
        ```
        
3. **Instalar Django en el entorno virtual:**
    
    ```
    pip install django
    ```
    
    - Comprobar la versión de Django
        
        ```sql
        python -m django --version
        ```
        
    instalar pillows

    ```
    python -m pip install Pillow
    ```

- Moverse a la carpeta del proyecto 

```
cd ecommerce
```

- Ejecutar el servidor:
        
        ```bash
        python manage.py runserver
        ```
        
Acceder a tu sitio en `http://127.0.0.1:8000/`.

4. **pasos por si se inicia el proyecto de 0 - Crear un proyecto Django:**
    
    ```
    django-admin startproject ecommerce_project
    cd ecommerce_project
    ```
    
5. **Crear una aplicación dentro del proyecto para gestionar los productos.:**
    
    ```
    python manage.py startapp store
    ```
    
6. **Crear una aplicación dentro del proyecto para administrar**
    
    ```
    python manage.py startapp administration
    ```
    
7. Configurar el proyecto:
- En `ecommerce/settings.py`, agrega 'store' y 'administration' a `INSTALLED_APPS`.
    
    ```sql
    INSTALLED_APPS = [
    		'store',
        'administration',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```
    
- Configura la base de datos (por defecto es SQLite).
    
    ### SQLite and DataGrip
    
    Para conectarte a una base de datos SQLite que estás utilizando con Django mediante DataGrip, sigue estos pasos:
    
    ### Paso 1: Configura tu base de datos en Django
    
    Asegúrate de que tu archivo `settings.py` en tu proyecto de Django esté correctamente configurado para tu base de datos SQLite. Por ejemplo:
    
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```
    
    ### Paso 2: Localiza tu archivo de base de datos
    
    Por defecto, Django crea el archivo de la base de datos SQLite en el directorio base de tu proyecto con el nombre `db.sqlite3`. Asegúrate de conocer la ruta completa a este archivo.
    
    ### Paso 3: Abre DataGrip y configura una nueva conexión

    [jetbrains Student Pack](https://www.jetbrains.com/community/education/#students)
    
    1. **Abre DataGrip** y ve a `File > Data Sources and Drivers`.
    2. **Añade una nueva conexión** seleccionando `SQLite`.
    
    ### Paso 4: Configura los parámetros de conexión
    
    3. En la ventana de configuración, selecciona el archivo de tu base de datos SQLite:
        - **Database file**: Navega y selecciona el archivo `db.sqlite3` en tu proyecto Django.
    
    ### Paso 5: Prueba la conexión
    
    4. Haz clic en el botón **Test Connection** para asegurarte de que DataGrip puede conectarse a tu base de datos.
    5. Si la conexión es exitosa, verás un mensaje de éxito.
    
    ### Paso 6: Explora tu base de datos
    
    6. Una vez que la conexión esté establecida, podrás ver tu base de datos en el panel de DataGrip.
    7. Podrás ejecutar consultas SQL, explorar tablas y ver datos directamente desde DataGrip.
- Agrega la carpeta de medios:
Crea carpetas `static` y `media` en la raíz del proyecto.

agregar en el mismo archivo `ecommerce/settings.py` 

- `import os` y mas abajo
    
    ```sql
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```
    

Configuración de archivos estáticos

1. **Crear la estructura de archivos estáticos:**
Dentro de la carpeta `store`, crea una carpeta `static` y dentro de ella una subcarpeta `images` para almacenar las fotos de los productos.
2. **Configurar `settings.py` para archivos estáticos en `ecommerce/settings.py`**
    
    ```sql
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    ```
    
3. Crear modelos para Productos y Usuarios: ?Modelos van juntos o separados? van solo en el folder store? por que no en administration o por que no en ambos?
En `store/models.py`:

```sql
from django.db import models

# Create your models here.
# store/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10)
    image = models.ImageField(upload_to='products/')

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Usaremos hash de contraseñas
    is_admin = models.BooleanField(default=False)

```

Crear Vistas y plantillas

1. Configurar las URLs:
    
    en `ecommerce_project/urls.py` se agrega `from django.urls import path, include` y queda de esta forma:
    
    ```sql
    # ecommerce_project/urls.py
    from django.contrib import admin
    from django.urls import path, include
    from django.conf import settings
    from django.conf.urls.static import static
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('store.urls')),
        path('administration/', include('administration.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    ```
    
    lo mismo en `store/urls.py`
    
    ```sql
    # store/urls.py
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.index, name='index'),
        path('about/', views.about, name='about'),
        path('products/', views.products, name='products'),
        path('login/', views.login_view, name='login'),
        path('logout/', views.logout_view, name='logout'),
    ]
    ```
    
    lo mismo en `administration/urls.py` pero para gestionar el CRUD
    
    ```sql
    
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('products/', views.admin_products, name='admin_products'),
        path('products/create/', views.create_product, name='create_product'),
        path('products/update/<int:product_id>/', views.update_product, name='update_product'),
        path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
        path('users/', views.admin_users, name='admin_users'),
        path('users/create/', views.create_user, name='create_user'),
        path('users/update/<int:user_id>/', views.update_user, name='update_user'),
        path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
        
    ]
    
    ```
    
2. Crear vistas básicas:
    
    `store/views.py`
    
    ```sql
    
    from django.shortcuts import render, redirect
    from django.contrib import messages
    from .models import Product, CustomUser
    
    def index(request):
        products = Product.objects.all()
        return render(request, 'index.html', {'products': products})
    
    def login_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = CustomUser.objects.get(username=username, password=password)
                request.session['user_id'] = user.id
                request.session['is_admin'] = user.is_admin
                return redirect('index')
            except CustomUser.DoesNotExist:
                messages.error(request, 'Invalid login credentials')
        return render(request, 'login.html')
    
    def admin_view(request):
        if not request.session.get('is_admin', False):
            return redirect('index')
        return render(request, 'admin.html')
    
    def product_list(request):
        products = Product.objects.all()
        return render(request, 'products.html', {'products': products})
    
    def admin_products(request):
        if not request.session.get('is_admin', False):
            return redirect('index')
        products = Product.objects.all()
        return render(request, 'admin_products.html', {'products': products})
    
    def admin_users(request):
        if not request.session.get('is_admin', False):
            return redirect('index')
        users = CustomUser.objects.all()
        return render(request, 'admin_users.html', {'users': users})
    
    ```
    
    `administration/views.py`
    
    ```sql
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
    ```
    
    1. Crear y aplicar migraciones:
        
        ```sql
        python manage.py makemigrations store
        python manage.py migrate
        ```
        
        - En mi caso me salio el siguiente error:
        
        ```sql
        (myenv) PS E:\Desarrollo\OtrosProyectos\e-commerce\ecommerce> python manage.py makemigrations store
        SystemCheckError: System check identified some issues:
        
        ERRORS:
        store.Product.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
                HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
        ```
        
        instale pillow con: `python -m pip install Pillow`
        
        después corri el comando `python [manage.py](http://manage.py/) makemigrations store`
        
        y ejecute el comando `python [manage.py](http://manage.py/) migrate`
        
    - Crear un superusuario (opcional, para acceder al admin de Django):
        
        ```bash
        python manage.py createsuperuser
        ```
        
    - Ejecutar el servidor:
        
        ```bash
        python manage.py runserver
        ```
        
        Acceder a tu sitio en `http://127.0.0.1:8000/`.
        
    
3. Crear plantillas utilizando Bootstrap:
    
    
    Crea una carpeta `templates` dentro de la aplicación `store` y añade archivos HTML como `index.html`, `login.html`, `products.html`, . Asegúrate de incluir Bootstrap en tus plantillas.
    
    `Continuar editando otras views`
    
    a partir de aquí configure el proyecto para tener la lógica de administrador separado y genere varias vistas en administration donde cambie de carpetas algunos templates de store a la carpeta administration/templates

# Dia 2

 ### Agrege

 **- DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'** en `settings.py` de `ecommerce`

 


## Queda pendiente

- [x]  Logearse como admin y ejecutar CRUD de productos y usuarios
- [x]  Mis productos (lista con las fotos, nombres y precios de los productos, 10
productos). Los productos son leídos desde la tabla Productos y reflejados en la
página. La foto debe estar en una carpeta de fotos ( en nuestro caso media ) y en la tabla solo el nombre de la foto.
- [x] Quiénes Somos (nombre y foto de los dos integrantes)
- [x] Login (esta opción permite ingresar al administrador de usuarios y productos). Alcerrar la sesión desaparece la opción Administración del Navbar
- [x] El sistema debe enviar un mensaje de error si es que el usuario no se pudo logear.


## Importante
  ### Revisar
  - [x] No debe usar la tabla User de Django
  - [x] Logout
  - [ ] Ajustar Template´s con un diseño mas atractivos y con bootstrap

## Proyecto aun en desarrollo
