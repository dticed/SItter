from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'sitter/home.html', context)


def home2(request):
    return render(request, 'sitter/home2.html')

class PostListView(LoginRequiredMixin, ListView):
    model = Post 
    template_name = 'sitter/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #ordena por data

class PostDetailView(DetailView):
    model = Post 

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/home2/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False