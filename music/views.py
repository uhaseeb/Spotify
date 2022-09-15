from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login, logout
from .forms import SearchForm, CreatePlaylistForm, FavouritesForm
from users.forms import SignupForm, LoginForm
from .models import Track, Album, Artist, Genre, Playlist
from users.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from rest_framework import serializers, exceptions
from rest_framework import generics
from .serializers import TrackSerializer, AlbumSerializer, ArtistSerializer
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class IndexAPIView(APIView):
    def get(self, request, *args, **kwargs):
        request.query_params
        if request.query_params is not {}:
            search = request.query_params.get('search', '')
            track = Track.objects.filter(name__icontains=search)
            track_serializer = TrackSerializer(track, many=True)
            album = Album.objects.filter(name__icontains=search)
            album_serializer = AlbumSerializer(album, many=True)
            artist = Artist.objects.filter(name__icontains=search)
            artist_serializer = ArtistSerializer(artist, many=True)
            context = {'track_serializer': track_serializer.data, 'album_serializer': album_serializer.data, 'artist_serializer': artist_serializer.data}
            return Response(context)

        else:
            track = Track.objects.all()
            track_serializer = TrackSerializer(track, many=True)
            album = Album.objects.all()
            album_serializer = AlbumSerializer(album, many=True)
            artist = Artist.objects.all()
            artist_serializer = ArtistSerializer(artist, many=True)
            context = {'track_serializer': track_serializer.data, 'album_serializer': album_serializer.data, 'artist_serializer': artist_serializer.data}
            return Response(context)


class TrackDetail(APIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    def get(self, request, pk, *args, **kwargs):
        track = Track.objects.get(id=pk)
        if track is not None:
            tracks = TrackSerializer(track)
            return Response(tracks.data)


class AlbumDetail(APIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get(self, request, pk, *args, **kwargs):
        album = Album.objects.get(id=pk)
        if album is not None:
            albums = AlbumSerializer(album)
            return Response(albums.data)


class ArtistDetail(APIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, pk, *args, **kwargs):
        artist = Artist.objects.get(id=pk)
        if artist is not None:
            artists = ArtistSerializer(artist)
            return Response(artists.data)

#
