from django.contrib.auth.views import logout_then_login
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login, logout
from .forms import SearchForm
from users.forms import SignupForm, LoginForm
from .models import Track, Album, Artist, Genre, Playlist
from users.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, View):
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
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


class TrackDetailView(View):

    def get(self, request, id):
        track = Track.objects.get(id=id)
        context = {'track': track}
        return render(request, 'song_detail.html', context)


class AllTracksView(ListView):
    model = Track
    template_name = 'all_songs.html'
    context_object_name = 'all_songs'


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
    form_class = SignupForm
    template_name = 'signup.html'


class CreateUserView(View):
    model = User
    form_class = SignupForm

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            gender = form.cleaned_data['gender']

            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return HttpResponseRedirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return HttpResponseRedirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, gender=gender)
                user.save()
                user.playlists.create(name='liked_songs')
                return HttpResponseRedirect('/music')

        return render(request, 'signup.html', {'form': form})

    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})


class LoginView(CreateView):
    template_name = 'login.html'
    model = User
    fields = ['username', 'password']


class LoginAuthView(View):
    model = User
    form_class = LoginForm
    template_name = 'login.html'

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/music')

        else:
            messages.info(request, "user credentials invalid")
            return HttpResponseRedirect('login')

    def get(self, request):
        form = LoginForm()

        return render(request, 'login.html', {'form': form})


class LogoutView(View):

    def post(self, request):
        logout(request)
        return HttpResponse('user logged out')

    def get(self, request):
        logout(request)
        return HttpResponse("user logged out")


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(username=request.user)
        all_playlists = user.playlists.all()
        context = {'user': user, 'all_playlists': all_playlists}
        return render(request, 'user_detail.html', context)
