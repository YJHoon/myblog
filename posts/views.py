from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'posts/main.html', {'posts': posts})


def new(request):
    return render(request, 'posts/new.html')


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        files = request.FILES.get('post_file')
        Post.objects.create(title=title, content=content, image=image, post_file = files)
        return redirect('posts:main')


def show(request, id):
    post = Post.objects.get(pk = id)
    post.view_count += 1
    post.save()
    return render(request, 'posts/show.html', {'post': post})


def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/edit.html', {'post': post})


def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.title = request.data['title']
        post.content = request.POST['content']
        post.image = request.FILES['image']
        post.save()
        return redirect('posts:show', post.id)


def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('posts:main')