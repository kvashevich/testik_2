from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homePageView, name = 'home') ,
    path('home', views.homePageView, name = 'home'),
]