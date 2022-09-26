from django.db import models
from django.contrib.auth.models import AbstractUser
from . import constants
from music.models import Playlist, Album, Artist, Track


class User(AbstractUser):
    gender = models.CharField(max_length=30, choices=constants.gender_choice, default='Male')

    def liked_songs(self, *all_tracks):
        liked_songs = self.playlists.create(name=f"{self.username}_liked_songs")
        liked_songs.track.add(*all_tracks)
        return liked_songs



