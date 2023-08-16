from django.db import models
from .user import User
from .park import Park

class Trail(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trail_name = models.CharField(max_length=50)
    park_id = models.ForeignKey(Park, on_delete=models.CASCADE)
    length = models.CharField(max_length=100)
    rating = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
