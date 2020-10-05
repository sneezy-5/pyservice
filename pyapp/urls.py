from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name= 'acceuil'),
    path('contact', views.contact, name= 'contact')
]
