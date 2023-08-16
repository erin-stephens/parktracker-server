from django.db import models
from .user import User
from .park import Park

class Favorite(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    park = models.ForeignKey(Park, on_delete=models.CASCADE)
