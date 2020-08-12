from django.conf.urls import url
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^post/', views.post, name='post'),
    url(r'^publish/', views.publish, name='publish'),
    url(r'^read/', views.read, name='read'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
