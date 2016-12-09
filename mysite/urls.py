from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
