from django.urls import path, include
from .views import main, create, update, show, delete

app_name = "posts"
urlpatterns = [
  path('', main, name="main"),
  path('create/', create, name="create"),
  path('update/', update, name="update"),
  path('show/<int:id>/', show, name="show"),
  path('delete/<int:id>/', delete, name="delete"),
]