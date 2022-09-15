from django.db import models
from django.contrib.auth import get_user_model
import time
User = get_user_model()


class Track(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='tracks')
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='tracks')
    genre = models.ManyToManyField('Genre', related_name='tracks')
    length = models.PositiveIntegerField()
    thumbnail = models.CharField(max_length=50)
    song = models.FileField(upload_to='mp3')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    @property
    def duration(self):
        converted_format = time.strftime("%H:%M:%S", time.gmtime(self.length))
        return converted_format

    def __str__(self):
        return f"{self.name}"


class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return f"{self.name}"


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    track = models.ManyToManyField('Track', related_name='playlists')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')

    def __str__(self):
        return f"{self.name}"
