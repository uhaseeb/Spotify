from music.models import Track, Album, Artist, Genre, Playlist
from users.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import serializers, exceptions
from rest_framework import generics
from .serializers import TrackSerializer, AlbumSerializer, ArtistSerializer, UserLoginSerializer, CreateTrackSerializer, UpdateTrackSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.urls import reverse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class IndexAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):

        search = request.query_params.get('search', '')

        track = Track.objects.filter(name__icontains=search)[:10]
        tracks = TrackSerializer(track, many=True)

        album = Album.objects.filter(name__icontains=search)[:10]
        albums = AlbumSerializer(album, many=True)

        artist = Artist.objects.filter(name__icontains=search)[:10]
        artists = ArtistSerializer(artist, many=True)

        context = {'tracks': tracks.data, 'album_serializer': albums.data,
                   'artists': artists.data}
        return Response(context)


class TrackDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Track.objects.all()
    model = Track
    serializer_class = UpdateTrackSerializer
    # def get(self, request, pk, *args, **kwargs):
    #     track = Track.objects.get(id=pk)
    #     tracks = TrackSerializer(track)
    #     return Response(tracks.data)
    #


class AlbumDetailAPIView(APIView):
    queryset = Album.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        album = Album.objects.get(id=pk)
        albums = AlbumSerializer(album)
        return Response(albums.data)


class ArtistDetailAPIView(APIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        artist = Artist.objects.get(id=pk)
        artists = ArtistSerializer(artist)
        return Response(artists.data)


class TracksListingAPIView(generics.ListAPIView):
    queryset = Track.objects.all().order_by('-id')
    serializer_class = TrackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['id', 'name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class LoginAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid()
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)

            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": user.username
            })


# class CreateTrackAPIView(generics.CreateAPIView):
#     serializer_class = TrackSerializer
#     queryset = Track.objects.all()
#     model = Track

class CreateTrackAPIView(generics.CreateAPIView):
    serializer_class = CreateTrackSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    model = Track
    queryset = Track.objects.all()




