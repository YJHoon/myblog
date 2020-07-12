from django.urls import path
from .views import main, new, create

app_name="posts"
urlpatterns = [
    path('', main, name="main"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
]