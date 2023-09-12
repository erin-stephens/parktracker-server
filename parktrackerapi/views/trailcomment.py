from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parktrackerapi.models import TrailComment, Trail, User

class TrailCommentView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single comment

        Returns:
            Response -- JSON serialized comment
        """
        comment = TrailComment.objects.get(pk=pk)
        serializer = TrailCommentSerializer(comment)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all comments

        Returns:
            Response -- JSON serialized list of comments
        """
        comments = TrailComment.objects.all()
        trail_comments = request.query_params.get('trail_id', None)
        if trail_comments is not None:
                comments = comments.filter(trail_id=trail_comments)
        serializer = TrailCommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        trail_id = Trail.objects.get(pk=request.data["trailId"])
        author_id = User.objects.get(pk=request.data["authorId"])
        
        comment = TrailComment.objects.create(
            content=request.data["content"],
            trail_id=trail_id,
            author_id=author_id
        )
        serializer = TrailCommentSerializer(comment)
        return Response(serializer.data)
    
    def update(self, request, pk):
        comment = TrailComment.objects.get(pk=pk)
        comment.content = request.data["content"]
        
        trail_id = Trail.objects.get(pk=request.data["trailId"])
        comment.trail_id = trail_id
        author_id = User.objects.get(pk=request.data["authorId"])
        comment.author_id = author_id
        comment.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        comment = TrailComment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class TrailCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= TrailComment
        fields = ('id', 'trail_id', 'author_id', 'content')
