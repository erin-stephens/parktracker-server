from django.db import models
from .user import User
from .trail import Trail

class TrailComment(models.Model):

    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    trail_id = models.ForeignKey(Trail, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
