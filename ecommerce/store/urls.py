from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('consultar-api/', views.consultar_api, name='consultar_api'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
