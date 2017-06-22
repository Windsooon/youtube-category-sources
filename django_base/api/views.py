from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from inner.models import Inner
from inner.serializers import InnerSerializer
from playlist.models import Playlist
from playlist.serializers import PlaylistSerializer
from .permissions import IsAdminOrReadOnly


class DefaultsMixin(object):
    permission_classes = (IsAdminOrReadOnly, )
    paginate_by = 20


class InnerViewSet(viewsets.ModelViewSet):
    queryset = Inner.objects.all()
    serializer_class = InnerSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly, )
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'inner': reverse('inner_list', request=request, format=format),
        'playlist': reverse('playlist_list', request=request, format=format)
    })
