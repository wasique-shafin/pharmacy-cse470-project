from django.contrib import admin
from django.urls import path

from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MVC.routes',namespace='MVC')),
]

# Media Folder
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
