from django.urls import path
from .views import (
    admin_products, create_product, update_product, delete_product,
    admin_users, create_user, update_user, delete_user
)

urlpatterns = [
    # Rutas para productos
    path('products/', admin_products, name='admin_products'),
    path('products/new/', create_product, name='create_product'),
    path('products/<int:product_id>/edit/', update_product, name='update_product'),
    path('products/<int:product_id>/delete/', delete_product, name='delete_product'),

    # Rutas para usuarios
    path('users/', admin_users, name='admin_users'),
    path('users/new/', create_user, name='create_user'),
    path('users/<int:user_id>/edit/', update_user, name='update_user'),
    path('users/<int:user_id>/delete/', delete_user, name='delete_user'),
]
