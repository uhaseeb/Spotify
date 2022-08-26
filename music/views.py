from django.shortcuts import render
from django.views.generic import View
from .forms import SearchForm
from .models import Track, Album, Artist, Genre, Playlist
from django.http import HttpResponse

class IndexView(View):
    template_name = 'index.html'
    form = SearchForm

    def post(self, request):
        search = request.POST['search']
        form = SearchForm(request.POST)
        if Track.objects.filter(track_name=search):
            songs = Track.objects.filter(track_name=search)
            is_song = True
            context = {'songs': songs, 'is_song': is_song, 'form': form}
            return render(request, 'index.html', context)

        elif Album.objects.filter(album_name=search):
            albums = Album.objects.filter(album_name=search)
            is_album = True
            context = {'albums': albums, 'is_album': is_album, 'form': form}
            return render(request, 'index.html', context)

        elif Artist.objects.filter(artist_name=search):
            artists = Artist.objects.filter(artist_name=search)
            is_artist = True
            context = {'artists': artists, 'is_artist': is_artist, 'form': form}
            return render(request, 'index.html', context)

        else:
            return HttpResponse("no record found")

    def get(self, request):
        form = SearchForm()

        return render(request, 'index.html', {'form': form})
