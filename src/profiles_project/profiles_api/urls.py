from django.conf.urls import url
from django.contrib import admin

# DRF has Router to set up different URL for viewsets
from rest_framework.routers import DefaultRouter

# always import include before use it!
from django.conf.urls import include
from .views import (
    HelloAPIView,
    HelloViewSet,
    UserProfileViewSet,
    LoginViewSet
    )


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name = 'hello-viewset')
# DRF automatically find base_name so we don't need to specify base_name
router.register('profile', UserProfileViewSet)
# it's not module viewset so we need to specify base_name
router.register('login', LoginViewSet, base_name = 'login')

urlpatterns = [
    url(r'^hello-view/', HelloAPIView.as_view(), name='hello'),
    url(r'^', include(router.urls))
]
