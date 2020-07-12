from django.shortcuts import render, redirect
from .models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'posts/main.html')


def new(request):
    return render(request, 'posts/new.html')


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('main')


def show(request, id):
    post = Post.objects.get(pk = id)
    return render(request, 'posts/show.html')