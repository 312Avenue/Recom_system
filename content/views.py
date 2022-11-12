from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import ContentSerializers, FavoritesSerializer
from .models import Content, Favorites


class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializers
    filterset_fields = ['genre', 'author', 'title']
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'text', 'author']
    permission_classes = [permissions.AllowAny]
        
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    @action(['GET', 'POST'], detail=True)
    def favorite(self, request, pk=None):
        content = self.get_object()
        user = request.user
        try:
            favorites = Favorites.objects.filter(favorites_id=content, author_id=user)
            mauler = not favorites[0].favorites
            if mauler:
                favorites[0].save()
            else:
                favorites.delete()
            message = 'В избранном' if favorites else 'Не в избранном'
        except IndexError:
            Favorites.objects.create(favorites_id=content.id, author_id=user, yes_no=True)
            message = 'В избранном'
        return Response(message, status=200)


class PopularContentView(mixins.ListModelMixin, GenericViewSet):
    queryset = Content.objects.order_by('favorites')
    serializer_class = ContentSerializers


class NewContentView(mixins.ListModelMixin, GenericViewSet):
    queryset = Content.objects.order_by('-id')
    serializer_class = ContentSerializers


class MyFavoritesView(mixins.ListModelMixin, GenericViewSet):
    queryset = Favorites.objects.filter()
    serializer_class = FavoritesSerializer


# class FavoritesView(mixins.ListModelMixin, GenericViewSet):
#     queryset = Favorites.objects.all()
#     serializer_class = FavoritesSerializer