from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Courses', views.Courses, name='Courses'),
    path('Contact', views.Contact, name='Contact'),
    path('Login', views.Login, name='Login'),
    path('Events', views.Events, name='Events'),
    path('Fees', views.Fees, name='Fees'),
    path('Registration', views.Registration, name='Registration'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('Computer', views.Computer, name='Computer'),
    path('Mechanical', views.Mechanical, name='Mechanical'),
    path('Civil', views.Civil, name='Civil'),
    path('Information', views.Information, name='Information'),
    path('AI', views.AI, name='AI'),
    path('Data', views.Data, name='Data'),
    
]