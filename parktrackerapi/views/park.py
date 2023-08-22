"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from parktrackerapi.models import Park, User, Favorite


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
        """uid = request.data['uid']
        user = User.objects.get(uid=uid)
        
        for park in parks:
            park.favorited = len(Favorite.objects.filter(user=user, park=park)) > 0"""
        serializer = ParkSerializer(parks, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        """POST"""
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
    
    @action(methods=['post'], detail=True)
    def favorite(self, request, pk):
        user = User.objects.get(uid =request.data["userId"])
        park = Park.objects.get(pk=pk)
        favorited = Favorite.objects.create(
            user=user,
            park=park
        )
        return Response({'message': 'Favorite added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def unfavorite(self, request, pk):
        user = User.objects.get(uid = request.data["userId"])
        park = Park.objects.get(pk=pk)
        favorited = Favorite.objects.get(
            user_id = user.id,
            park_id = park.id
        )
        favorited.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['get'], detail=True)
    def get_favorites(self, request, pk):
        try:
            favorites = Favorite.objects.filter(park_id = pk)
            serializer = FavoriteSerializer(favorites, many=True)
            return Response(serializer.data)
        except Favorite.DoesNotExist:
            return Response(False)

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta: 
        model: Favorite
        fields = ('id', 'user', 'park')
        depth = 1

class ParkSerializer(serializers.ModelSerializer):
    """JSON serializer for parks"""
    class Meta: 
        model = Park
        fields = ('id', 'user', 'park_name', 'image_url', 'location', 'park_type', 'favorited')
        depth = 1
