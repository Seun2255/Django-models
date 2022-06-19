from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Room(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(null=True, blank=True)
    Author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title