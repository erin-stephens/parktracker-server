from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parktrackerapi.models import Site, User, Park


class SiteView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        
        site = Site.objects.get(pk=pk)
        serializer = SiteSerializer(site)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        sites = Site.objects.all()
        park_name = request.query_params.get('park', None)
        if park_name is not None:
            sites = sites.filter(park_id=park_name)
            
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        user = User.objects.get(uid=request.data["userId"])
        park_id = Park.objects.get(pk=request.data["parkId"])
        site = Site.objects.create(
          user=user,
          park_id=park_id,
          site_name=request.data["siteName"],
          image_url=request.data["imageUrl"],
          site_type=request.data["siteType"],
          description=request.data["description"],
        )
        serializer = SiteSerializer(site)
        return Response(serializer.data)
      
    def update(self, request, pk):
      
        site = Site.objects.get(pk=pk)
        site.site_name=request.data["siteName"]
        site.image_url=request.data["imageUrl"]
        site.site_type=request.data["siteType"]
        site.description=request.data["description"]
        park_id = Park.objects.get(pk=request.data["parkId"])
        site.park_id = park_id
        site.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    def destroy(self, request, pk):
        site = Site.objects.get(pk=pk)
        site.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SiteSerializer(serializers.ModelSerializer):

    class Meta: 
      model = Site
      fields = ('id', 'user', 'site_name', 'park_id', 'image_url', 'description', 'site_type')
      depth = 1
