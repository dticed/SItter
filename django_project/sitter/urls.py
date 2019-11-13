from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="sitter-home"),
    path('about/', views.about, name="sitter-about"),
]
