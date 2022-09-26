from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexAPIView.as_view(), name='index_page'),
    path('track_detail/<int:pk>', views.TrackDetail.as_view(), name='track_detail'),
    path('album_detail/<int:pk>', views.AlbumDetail.as_view(), name='album_detail'),
    path('artist_detail/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),

]
