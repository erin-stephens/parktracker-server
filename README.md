## ParkTracker
This is the server side repo to the ParkTracker application. ParkTracker serves as a space to organize your past and future trips to National or State Parks by adding trails and sites you've seen along the way.

## Motivation For This Project
This project came about when a few different friends asked me for recommendations on where to go in National Parks and I could not remember which trails I had hiked or sites I had seen. With ParkTracker, I can make a list that will organize all of this for future recommendations. 
 
## Link to FrontEnd Repo
[https://github.com/erin-stephens/parktracker-client]

## Tech/framework used

<b>Built with</b>
- [Django]([https://www.djangoproject.com/])

## Features
Users are able to create, read, update, delete parks, trails, and sites with this application. They can also favorite parks to add them to their own list on a separate page for future use. 

## Code Example
Below is a snapshot of creating, reading, and deleting parks data in the backend.

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        parks = Park.objects.all()
        uid = request.META['HTTP_AUTHORIZATION']
        user = User.objects.get(uid=uid)
        
        for park in parks:
            park.favorited = len(Favorite.objects.filter(user=user, park=park)) > 0
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
    
    def destroy(self, request, pk):
        park = Park.objects.get(pk=pk)
        park.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

## How to use?
Use this repo with the linked frontend repo to create your own ParkTracker items! 
