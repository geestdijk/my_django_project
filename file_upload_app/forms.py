from django import forms
from .models import AlbumFile, AvatarImage


class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumFile
        fields = ['description', 'image',]


class AvatarForm(forms.ModelForm):
    class Meta:
        model = AvatarImage
        fields = ['image',]

