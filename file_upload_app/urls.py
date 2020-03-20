from django.urls import re_path

from file_upload_app import views

app_name = 'album'

urlpatterns = [
    re_path(r'^album-upload/$', views.upload_album, name='album_upload'),
]