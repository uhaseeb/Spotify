from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView
from .forms import SearchForm
from users.forms import AuthenticationForm
from .models import Track, Album, Artist, Genre, Playlist
from users.models import User
from django.contrib.auth import authenticate, login


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


class SongDetailView(View):
    def get(self, request, id):
        track = Track.objects.get(id=id)
        context = {'track': track}
        return render(request, 'song_detail.html', context)


class AlbumDetailView(View):
    def get(self, request, id):
        album = Album.objects.get(id=id)
        all_tracks = album.tracks.all()
        context = {'album': album, 'all_tracks': all_tracks}
        return render(request, 'album_detail.html', context)


class ArtistDetailView(View):
    def get(self, request, id):
        artist = Artist.objects.get(id=id)
        all_albums = artist.albums.all()
        context = {'artist': artist, 'all_albums': all_albums}
        return render(request, 'artist_detail.html', context)


class SignupView(CreateView):
    model = User
    form_class = AuthenticationForm
    template_name = 'signup.html'


class CreateUserView(View):
    model = User
    form_class = AuthenticationForm, SearchForm

    def post(self, request):
        return render(request, 'index.html')

    def get(self, request):
        return