from django.urls import path
from . import views

urlpatterns = [
    path('app2home', views.app2home, name='app2home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('contact', views.contact, name='contact'),
        
]

