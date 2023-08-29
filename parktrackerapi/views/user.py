from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parktrackerapi.models import User, Favorite
from rest_framework.decorators import action

class UserView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=True)
    def get_favorites(self, request, pk):
        try:
            favorite = Favorite.objects.filter(
                user_id = pk,
            )
            serializer = FavoriteSerializer(favorite, many=True)
            return Response(serializer.data)
        except Favorite.DoesNotExist:
            return Response(False)

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Favorite
        fields = ('id', 'user', 'park')
        depth = 1
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'uid', 'first_name', 'last_name', 'bio')
