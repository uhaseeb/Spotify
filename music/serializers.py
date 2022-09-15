from rest_framework import serializers
from .models import Track, Album, Artist, Playlist


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Track


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Artist


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Album