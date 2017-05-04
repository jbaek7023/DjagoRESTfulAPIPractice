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
