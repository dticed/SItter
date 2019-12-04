from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'sitter/home.html', context)


def home2(request):
    return render(request, 'sitter/home2.html')

def about(request):
    return render(request, 'sitter/about.html', {'title': 'About'})