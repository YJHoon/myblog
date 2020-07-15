from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'posts/main.html', {'posts': posts})


def new(request):
    return render(request, 'posts/new.html')


def create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('posts:main')


def show(request, id):
    # post = get_object_or_404(Post, pk=id)
    post = Post.objects.get(pk=id)
    return render(request, 'posts/show.html', {'post': post})


def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:main', post.id)
    return render(request, 'posts/update.html', {'post': post})