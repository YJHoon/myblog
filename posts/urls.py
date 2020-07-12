from django.urls import path
from .views import main, new, create, show, edit, update, delete

app_name="posts"
urlpatterns = [
    path('', main, name="main"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('show/<int:id>/', show, name="show"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
]