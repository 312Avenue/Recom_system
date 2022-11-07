from django.urls import path
from .views import ContentViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('content', ContentViewSet)

urlpatterns = []
urlpatterns += router.urls # urlpatterns.extend(router.urls)