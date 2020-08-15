from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.
def main(request):
  posts = Post.objects.all()
  return render(request, 'posts/main.html', {"posts":posts})


def create(request):
  if request.method == "POST":
    title = request.POST.get("title")
    content = request.POST.get("content")
    post = Post.objects.create(title=title, content=content)
    return redirect('posts:show', post.pk)
  return render(request, 'posts/create.html')


def update(request, id):
  post = get_object_or_404(Post, pk=id)
  if request.method == "POST":
    post.title = request.POST.get()
    post.content = request.POST.get("content")
    post.save()
    return redirect('posts:show', post.pk)
  return render(request, 'posts/update.html', {"post": post})


def show(request, id):
  post = get_object_or_404(Post, pk=id)
  post.view_count += 1
  post.save()
  return render(request, 'posts/show.html', {"post": post})


def delete(request, id):
  post = get_object_or_404(Post, pk=id)
  post.delete()
  return redirect('posts:main')