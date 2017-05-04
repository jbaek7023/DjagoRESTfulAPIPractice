# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render



# get response object from rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Status has different HTTP Status Code
from rest_framework import status
from rest_framework import viewsets

from . import serializers
from . import models
from . import permissions

# token authentication : the most effective way
from rest_framework.authentication import TokenAuthentication

# restframework filters module
from rest_framework import filters

# DRF has login-API view to take care of Login
# But it fakes APIView and it doesn't have viewsets
# We don't have router for that!
# So we need to trick it
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

# Create your views here.
class HelloAPIView(APIView):
    """Test API View."""

    # serializer class is HelloSerializer for this view
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView Features."""

        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'It is mapped manually to URLs'
        ]
        # Response object always holds JSON Object
        return Response({
            'message': 'Hello World!',
            'an_apiview': an_apiview
        })

    def post(self, request):
        """Create Hello Message with our name"""
        # pass data in HelloSerializer
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            # Retrieve specific field name (in serializers specified)
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({
                'message': message
            })
        else:
            # errors dictionary assigned to the serializer
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields required"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes and object"""
        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return Hello Message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({
            'message': 'Hello World!', 'a_viewset': a_viewset
        })

    def create(self, request):
        """Create a new hello message."""
        # Define Serializer Object
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({
                'message': message
            })
        else:
            # errors dictionary assigned to the serializer
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""
        return Response({'http_method': 'GET'})

# pk is primary key
    def update(self, request, pk=None):
        """Handles updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles"""
    # It already knows which model to serializer
    # because since it's defined in UserProfileSerializer class
    serializer_class = serializers.UserProfileSerializer

    # List data
    queryset = models.UserProfile.objects.all()

    # authentication class variable
    # tuple : immutable list
    # don't forget the put the comma
    # U can put more than one authentication or permission... that's why we use token
    authentication_classes = (TokenAuthentication,)

    # Now you can't Delete or update it! U can only see it
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    """checks email and password and returns an auth token"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token"""
        # pass request and call the POST function
        # () <- making new object

        # it returns a temporary token
        # "token": "59a999eb165158d2b3c0713332c174d551fb0160"

        # the client has to ensure the token is included in every HTTP request
        # Authorization HTTP Header will include our token.
        # Then we can check if HTTP request has VALID token.
        # If the token is valid, 200.
        # If it's not valid. return 401 or authorize response to regenerate token!


        # HTTP header is like meta-data : data about request

        return ObtainAuthToken().post(request)

        # When u test on the browser, ensure that 'filter' is running.
        # To apply the token only the page

        # Add Authorization -> Token 59a999eb165158d2b3c0713332c174d551fb0160
