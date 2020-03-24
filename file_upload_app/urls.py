from django.urls import re_path
from file_upload_app import views

app_name = 'album'

urlpatterns = [
    re_path(r'^album-upload/$', views.album_upload, name='album_upload'),
    re_path(r'^avatar-upload/$', views.avatar_upload, name='avatar_upload'),
    re_path(r'^album-view-by-folder/(?P<folder_name>\d+)/$', views.album_view_by_folder, name='album_view_by_folder'),
    re_path(r'^view/(?P<user>\d+)/$', views.AlbumView.as_view(), name='album_view'),
    re_path(r'^delete/(?P<image_pk>\d+)/$', views.delete_image, name='delete_image'),
]
