from django.shortcuts import render
from django.views.generic import View
from .forms import SearchForm
from .models import Track, Album, Artist, Genre, Playlist


class IndexView(View):
    template_name = 'index.html'
    form = SearchForm

    def post(self, request):
        search = request.POST['search']
        form = SearchForm(request.POST)
        songs = Track.objects.filter(name__icontains=search)
        albums = Album.objects.filter(name__icontains=search)
        artists = Artist.objects.filter(name__icontains=search)
        context = {'artists': artists, 'songs': songs, 'albums': albums, 'form': form}
        return render(request, 'index.html', context)

    def get(self, request):
        form = SearchForm()
        return render(request, 'index.html', {'form': form})
