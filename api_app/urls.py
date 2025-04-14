from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'mangas', views.MangaViewSet, basename = 'mangas')
router.register(r'artists', views.ArtistViewSet, basename= 'artists')
urlpatterns = [
    path('mangas-library-v1/', include(router.urls)),
    path('mangas-library-v1/mangas/new-manga', views.new_manga, name='new-manga'),
]
