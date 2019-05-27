import patterns as patterns
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from demo.views import (
    ChunkedUploadDemo, MyChunkedUploadView, MyChunkedUploadCompleteView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',
        ChunkedUploadDemo.as_view(), name='chunked_upload'),
    url(r'^api/chunked_upload/?$',
        MyChunkedUploadView.as_view(), name='api_chunked_upload'),
    url(r'^api/chunked_upload_complete/?$',
        MyChunkedUploadCompleteView.as_view(),
        name='api_chunked_upload_complete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)