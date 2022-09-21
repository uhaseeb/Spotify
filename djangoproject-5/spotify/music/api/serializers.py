
from rest_framework import serializers
from music.models import Track, Album, Artist, Playlist, Genre
from users.models import User


class TrackSerializer(serializers.ModelSerializer):
    artist = serializers.CharField(required=True)
    album = serializers.CharField(required=True)
    genre = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'
        model = Track

    # def create(self, validated_data):
    #     artist_data = validated_data.pop('artist')
    #     artist, _ = Artist.objects.get_or_create(name=artist_data)
    #     album_data = validated_data.pop('album')
    #     album, _ = Album.objects.get_or_create(name=album_data, defaults={"artist": artist})
    #     genre_data = validated_data.pop('genre')
    #     genre, _ = Genre.objects.get_or_create(name=genre_data)
    #     track = Track.objects.create(**validated_data, album=album, artist=artist)
    #     track.genre.add(genre)
    #     return track


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Artist


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['artist']
        model = Album


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=60, label='Username')
    password = serializers.CharField(max_length=30, label='Password')


class CreateTrackSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    artist = ArtistSerializer()
    genre = GenreSerializer()

    class Meta:
        fields = ['artist', 'album', 'genre', 'name', 'length', 'thumbnail']
        model = Track

    def create(self, validated_data):
        artist_data = validated_data.pop('artist')['name']
        artist, _ = Artist.objects.get_or_create(name=artist_data)
        album_data = validated_data.pop('album')['name']
        album, _ = Album.objects.get_or_create(name=album_data, defaults={'artist': artist})
        genre_data = validated_data.pop('genre')['name']
        genre, _ = Genre.objects.get_or_create(name=genre_data)
        track = Track.objects.create(**validated_data, album=album, artist=artist)
        track.genre.add(genre)
        return track


class UpdateTrackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Track

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.album = validated_data.get('album', instance.album)
        instance.length = validated_data.get('length', instance.length)
        instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)

        instance.save()
        return instance
