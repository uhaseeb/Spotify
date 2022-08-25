from django.contrib import admin
from .models import Track, Album, Artist, Genre, Playlist


class TrackAdmin(admin.ModelAdmin):
    list_display = ("track_name", "album", "artist")


class AlbumAdmin(admin.ModelAdmin):
    list_display = ("album_name", "artist")


admin.site.register(Track, TrackAdmin)
admin.site.register(Artist)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre)
admin.site.register(Playlist)


