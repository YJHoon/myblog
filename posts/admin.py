from django.contrib import admin
from . import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=(
        'id', 
        'title',
        'view_count',
        'created_at'
    )

    search_field=(
        'title',
    )