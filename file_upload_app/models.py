from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    """Creates a path string to upload a file to a folder
    associated with the user id"""
    if isinstance(instance, AvatarImage):
        return f'avatars/user_{instance.user.id}/{filename}'
    elif isinstance(instance, AlbumFile):
        return f'albums/user_{instance.user.id}/{filename}'

class AbstractImage(models.Model):
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now=True)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        abstract = True


class AlbumFile(AbstractImage):
    pass
    
class AvatarImage(AbstractImage):
    description = models.CharField(max_length=255, default='')