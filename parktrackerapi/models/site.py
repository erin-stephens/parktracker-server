from django.db import models
from .user import User
from .park import Park

class Site(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=50)
    park_id = models.ForeignKey(Park, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    site_type = models.CharField(max_length=50)
