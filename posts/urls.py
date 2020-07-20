from django.urls import path
from .views import main, new, create, show, update, delete
from django.conf import settings
from django.conf.urls.static import static

app_name="posts"
urlpatterns = [
    path('', main, name="main"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('show/<int:id>/', show, name="show"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    # case 1
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# case2
