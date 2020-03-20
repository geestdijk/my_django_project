from django.urls import re_path

from file_upload_app import views

app_name = 'album'

urlpatterns = [
    re_path(r'^album_upload/$', views.upload_album, name='upload_album'),
]