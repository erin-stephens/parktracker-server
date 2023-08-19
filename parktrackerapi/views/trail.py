from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parktrackerapi.models import Trail, User, Park


class TrailView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        trail = Trail.objects.get(pk=pk)
        serializer = TrailSerializer(trail)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        trails = Trail.objects.all()
        serializer = TrailSerializer(trails, many=True)
        return Response(serializer.data)
      
    def create(self, request):
      
        user = User.objects.get(uid=request.data["userId"])
        park_id = Park.objects.get(pk=request.data["parkId"])
        trail = Trail.objects.create(
          user=user,
          park_id=park_id,
          trail_name=request.data["trailName"],
          length=request.data["length"],
          rating=request.data["rating"],
          description=request.data["description"],
        )
        serializer = TrailSerializer(trail)
        return Response(serializer.data)
      
    def update(self, request, pk):
      
        trail = Trail.objects.get(pk=pk)
        trail.trail_name=request.data["trailName"]
        trail.length=request.data["length"]
        trail.rating=request.data["rating"]
        trail.description=request.data["description"]
        park_id = Park.objects.get(pk=request.data["parkId"])
        trail.park_id = park_id
        trail.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
      
    def destroy(self, request, pk):
        trail = Trail.objects.get(pk=pk)
        trail.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class TrailSerializer(serializers.ModelSerializer):
  
    class Meta: 
      model = Trail
      fields = ('id', 'user', 'park_id', 'trail_name', 'length', 'rating', 'description')
      depth = 1
