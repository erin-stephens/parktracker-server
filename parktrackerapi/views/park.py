"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parktrackerapi.models import Park


class ParkView(ViewSet):
    """Parks view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        park = Park.objects.get(pk=pk)
        serializer = ParkSerializer(park)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        parks = Park.objects.all()
        serializer = ParkSerializer(parks, many=True)
        return Response(serializer.data)

class ParkSerializer(serializers.ModelSerializer):
    """JSON serializer for parks"""
    class Meta: 
        model = Park
        fields = ('id', 'user', 'park_name', 'image_url', 'location', 'park_type')
