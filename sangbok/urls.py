from django.urls import path, include
from django.contrib.auth.models import User
from .apps.songs.models import Song
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'lyrics', 'lyrics_formated']

# ViewSets define the view behavior.
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'songs', SongViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path("songs/", include("sangbok.apps.songs.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
