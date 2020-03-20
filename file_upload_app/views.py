from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import AlbumForm


def model_form_upload(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
    else:
        form = AlbumForm()
    return render(request, 'album_upload.html', {
        'form': form
    })
