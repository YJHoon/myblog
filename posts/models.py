from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    POST_TYPES = [
        (0, '파이썬'),
        (1, '루비'),
        (2, '자바'),
    ]
    title = models.CharField(max_length=50, null=False, verbose_name = "제목")
    content = models.TextField(verbose_name = "내용")
    view_count = models.IntegerField(default=0, verbose_name = "조회수")
    image = models.ImageField(upload_to='images/', null=True, verbose_name = "이미지")
    post_type = models.PositiveSmallIntegerField(choices=POST_TYPES, verbose_name = "게시글타입")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "생성시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name = "수정시간")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "생성시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name = "수정시간")