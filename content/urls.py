from django.urls import path
from .views import (ContentViewSet, PopularContentView, 
                    NewContentView, MyFavoritesView,)
                    # FavoritesView)

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('content', ContentViewSet)
router.register('popular', PopularContentView)
router.register('news', NewContentView)
router.register('users-favorites', MyFavoritesView)
# router.register('favorites', FavoritesView)

urlpatterns = []
urlpatterns += router.urls