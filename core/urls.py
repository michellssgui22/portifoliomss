from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexViews

urlpatterns = [
    path('', IndexViews.as_view(), name='index'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)