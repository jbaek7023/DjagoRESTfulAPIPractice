from django.conf.urls import url
from django.contrib import admin

# DRF has Router to set up different URL for viewsets
from rest_framework.routers import DefaultRouter

# always import include before use it!
from django.conf.urls import include
from .views import (
    HelloAPIView, HelloViewSet
    )


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name = 'hello-viewset')

urlpatterns = [
    url(r'^hello-view/', HelloAPIView.as_view(), name='hello'),
    url(r'^', include(router.urls))
]
