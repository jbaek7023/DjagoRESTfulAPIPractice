from django.conf.urls import url
from django.contrib import admin

# always import include before use it!
from django.conf.urls import include
from .views import HelloAPIView

urlpatterns = [
    url(r'^hello-view/', HelloAPIView.as_view(), name='hello')
]
