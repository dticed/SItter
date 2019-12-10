from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth.models import User


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
    ordering = ['-date_posted']  # ordena por data


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        emails = []
        for user in User.objects.all():
            emails.append(user.email)
        model = Post
        form.instance.author = self.request.user
        send_mail(form.instance.title, "E-mail para turma de "+ str(form.instance.author) +"\n" + form.instance.content, 'ifcecratosi@gmail.com', emails)
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

#def sendmail(request):
#        send_mail(
#        model.title,
#        model.content,
#        'ifcecratosi@gmail.com',
#        ['lucaspierrealencar@gmail.com'],
#    )
#        return HttpResponse("Enviado")

