from rest_framework import serializers

from .models import Content, Favorites


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['author', 'yes_no']
    
    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['content'] = f'http://127.0.0.1:8000/content/{instance.favorites}/'
        return represent


class ContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('title', 'author', 'album', 'genre', 'year', 'img', 'content')

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['favorites'] = sum([dict(i)['yes_no'] for i in FavoritesSerializer(instance.favorites.all(), many=True).data])
        return represent