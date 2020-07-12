from django.url import path
from .views import profile

app_name = "introduction"
urlpatterns = [
    path('profile/', profile, name="profile"),
]