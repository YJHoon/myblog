from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=(
        'id', 
        'title',
        'content',
        'post_type',
        'view_count',
        'created_at'
    )

    search_field=(
        'title',
    )