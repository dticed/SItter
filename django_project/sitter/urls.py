from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="sitter-home"),
    path('home2/', views.home2, name="sitter-home2"),
    path('about/', views.about, name="sitter-about"),
]
