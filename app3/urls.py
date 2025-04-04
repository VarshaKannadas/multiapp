from django.urls import path
from . import views

urlpatterns = [
    path('app3home', views.app3home, name='app3home'),
    path('detail', views.detail, name='detail'),
    path('register', views.register, name='register'),
]
