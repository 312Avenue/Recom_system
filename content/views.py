from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ContentSerializers
from .models import Content, Favorites
# Create your views here.


class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializers
    filterset_fields = ['genre', 'author', 'title']
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'text', 'author']

    @action(['GET', 'POST'], detail=True)
    def favorite(self, request, pk=None):
        content = self.get_object()
        user = request.user
        try:
            favorites = Favorites.objects.filter(content_id=content, author=user)
            mauler = not favorites[0].favorites
            if mauler:
                favorites[0].save()
            else:
                favorites.delete()
            message = 'В избранном' if favorites else 'Не в избранном'
        except IndexError:
            Favorites.objects.create(content_id=content.id, author=user, favorites=True)
            message = 'В избранном'
        return Response(message, status=200)