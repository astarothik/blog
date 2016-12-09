from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^comment_send/(?P<pk>\d+)/comment_send/$', views.comment_send, name='comment_send'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
]