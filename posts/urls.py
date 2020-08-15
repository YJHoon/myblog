from django.urls import path, include
from .views import main, create, update, show, delete, create_comment

app_name = "posts"
urlpatterns = [
  path('', main, name="main"),
  path('create/', create, name="create"),
  path('update/<int:id>', update, name="update"),
  path('show/<int:id>/', show, name="show"),
  path('delete/<int:id>/', delete, name="delete"),
  path('<int:post_id>/create_comment', create_comment, name="create_comment"),
]