from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from os import listdir
from django.views import generic
from .models import AlbumFile


from .forms import AlbumForm


def album_upload(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('home')
    else:
        form = AlbumForm()
    return render(request, 'album_upload.html', {
        'form': form
    })


def album_view_by_folder(request, folder_name):
    path = settings.MEDIA_ROOT
    img_list = listdir(path + f'/user_{folder_name}')
    image_folder = settings.MEDIA_URL + f'user_{folder_name}/'
    context = {'images': img_list, 'image_folder': image_folder}
    return render(request, 'album_view_by_folder.html', context)


class AlbumView(generic.ListView):
    model = AlbumFile
    context_object_name = 'images'
    template_name = 'album_view.html'

    def get_queryset(self):
        return AlbumFile.objects.filter(user=self.kwargs['user'])