# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# get response object from rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):
    """Test API View."""
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


# views.py: Application Logic End-Point
