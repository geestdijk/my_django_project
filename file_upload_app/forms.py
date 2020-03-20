from django import forms
from .models import AlbumFile


class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumFile
        fields = ['description', 'image',]

