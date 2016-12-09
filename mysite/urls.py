from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # r'^grappelli/', include('grappelli.urls'),
    # url(r'^ckeditor/', include('ckeditor.urls', namespace='ckeditor')),
]