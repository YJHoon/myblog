from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.models import User
import pdb

# Create your views here.
def main(request):
  posts = Post.objects.all()
  return render(request, 'posts/main.html', {"posts":posts})


def create(request):
  if request.user.is_authenticated:
    if request.method == "POST":
      title = request.POST.get("title")
      content = request.POST.get("content")
      image = request.FILES.get("image")
      post_type = request.POST.get("post_type")
      user = request.user
      post = Post.objects.create(title=title, content=content, image=image, post_type=post_type, user=user)
      return redirect('posts:show', post.pk)
    return render(request, 'posts/create.html')
  else:
    return redirect('account_login')


def update(request, id):
  if request.user.is_authenticated:
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
      post.title = request.POST.get("title")
      post.content = request.POST.get("content")
      post.image = request.FILES.get("image")
      post.post_type = request.POST.get("post_type")
      post.save()
      all_comments = post.comments.all().order_by('-created_at')
      return redirect('posts:show', post.pk)
    return render(request, 'posts/update.html', {"post": post, 'comments': all_comments})
  else:
    return redirect('account_login')


def show(request, id):
  if request.user.is_authenticated:
    post = get_object_or_404(Post, pk=id)
    post.view_count += 1
    post.save()
    return render(request, 'posts/show.html', {"post": post})
  else:
    return redirect('account_login')


def delete(request, id):
  if request.user.is_authenticated:
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('posts:main')
  else:
    return redirect('account_login')


def create_comment(request, post_id):
  if request.method == "POST":
    post = get_object_or_404(Post, pk=post_id)
    current_user = request.user
    comment_content = request.POST.get("content")
    Comment.objects.create(writer=current_user, post = post, content = comment_content)
    return redirect('posts:show', post.pk)