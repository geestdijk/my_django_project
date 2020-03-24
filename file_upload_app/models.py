from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    """Creates a path string to upload a file to a folder
    associated with the user id"""
    return f'user_{instance.user.id}/{filename}'


class AlbumFile(models.Model):
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now=True)