from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import  static


url_patterns = [
    path('api/', include('core.api_urls')),
    path('allauth/', include('allauth.urls')),
    path('', admin.site.urls),
]

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + url_patterns