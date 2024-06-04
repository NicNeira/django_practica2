# administration/urls.py

from django.urls import path
from .views import (
    admin_products, create_product, update_product, delete_product,
    admin_users, create_user, update_user, delete_user
)

urlpatterns = [
    # Rutas para productos
    path('products/', admin_products, name='product_list'),
    path('products/new/', create_product, name='product_create'),
    path('products/<int:product_id>/edit/', update_product, name='product_update'),
    path('products/<int:product_id>/delete/', delete_product, name='product_delete'),

    # Rutas para usuarios
    path('users/', admin_users, name='user_list'),
    path('users/new/', create_user, name='user_create'),
    path('users/<int:user_id>/edit/', update_user, name='user_update'),
    path('users/<int:user_id>/delete/', delete_user, name='user_delete'),
]
