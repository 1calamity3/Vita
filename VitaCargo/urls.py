from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import set_language


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('', include('profile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
