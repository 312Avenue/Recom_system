from rest_framework import serializers

from .models import Content, Favorites

class ContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['favorites'] = FavoritesSerializer(instance.favorites.all(), many=True).data
        represent['favorites'] = sum([dict(i)['favorites'] for i in represent['favorites']])
        return represent


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['author', 'content', 'favorites']

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['content'] = f'http://127.0.0.1:8000/content/{instance.content_id}'
        return represent