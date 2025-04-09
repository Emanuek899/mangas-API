from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'mangas', views.MangaViewSet, basename = 'mangas')
router_artist = routers.DefaultRouter()
router_artist.register(r'artists', views.ArtistViewSet, basename = 'artists')

urlpatterns = [
    path('api/mangas_library/', include(router.urls)),
    path('api/artists/', include(router_artist.urls)),
]
