from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('song/<int:id>', views.SongDetailView.as_view(), name='song_detail'),
    path('album/<int:id>', views.AlbumDetailView.as_view(), name='album_detail'),
    path('artist/<int:id>', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('create_user', views.CreateUserView.as_view(), name='create_user'),
]
