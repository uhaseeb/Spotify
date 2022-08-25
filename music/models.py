from django.db import models
from django.contrib.auth.models import AbstractUser


class Track(models.Model):
    track_name = models.CharField(max_length=50)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='track')
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='track')
    genre = models.ManyToManyField('Genre', related_name='track')
    length = models.CharField(max_length=10)
    thumbnail = models.CharField(max_length=50)
    song = models.FileField(upload_to='mp3')

    def __str__(self):
        return f"{self.track_name} {self.artist} {self.album}"


class Artist(models.Model):
    artist_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.artist_name}"


class Album(models.Model):
    album_name = models.CharField(max_length=50)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='album')

    def __str__(self):
        return f"{self.album_name}"


class Genre(models.Model):
    genre_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.genre_name}"


class Playlist(AbstractUser):
    playlist_name = models.CharField(max_length=50)
    track = models.ManyToManyField('Track', related_name= 'playlist')
    liked_songs = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f"{self.playlist_name} {self.username}"
