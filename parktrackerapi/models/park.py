from django.db import models
from .user import User

class Park(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    park_name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    park_type = models.CharField(max_length=50)

    @property
    def favorited(self):
        return self.__favorited
    
    @favorited.setter
    def favorited(self, value):
        self.__favorited = value
