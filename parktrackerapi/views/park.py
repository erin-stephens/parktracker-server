"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parktrackerapi.models import Park, User


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
      
    def create(self, request):
        """ POST"""
        user = User.objects.get(uid=request.data["userId"])
        park = Park.objects.create(
          user=user,
          park_name=request.data["parkName"],
          image_url=request.data["imageUrl"],
          location=request.data["location"],
          park_type=request.data["parkType"],
        )
        serializer = ParkSerializer(park)
        return Response(serializer.data)
      
    def update(self, request, pk):
        """PUT request"""
        park = Park.objects.get(pk=pk)
        park.park_name = request.data["parkName"]
        park.image_url = request.data["imageUrl"]
        park.location = request.data["location"]
        park.park_type = request.data["parkType"]
        
        park.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        park = Park.objects.get(pk=pk)
        park.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ParkSerializer(serializers.ModelSerializer):
    """JSON serializer for parks"""
    class Meta: 
        model = Park
        fields = ('id', 'user', 'park_name', 'image_url', 'location', 'park_type')
        depth = 1
