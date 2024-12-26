from django.contrib import admin
from django.urls import path , include
from Home import views 
from django.contrib.auth import views as auth
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.signup, name = "signup"),
    path("home/",views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("contact/", views.contact , name = "contact"),
    path("services/", views.services, name = "services"),
    path('login/', views.login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='Home/index.html'), name ='logout'),
]
