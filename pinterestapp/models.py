
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Pin(models.Model):
    title=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='pins/')
    website=models.URLField(max_length=200,blank=True)
    publishedon=models.DateTimeField(auto_now_add=True)
    createdby = models.ForeignKey(User, related_name="createdby",on_delete=models.CASCADE)



class Comments(models.Model):
    comment = models.TextField(max_length=256)
    commented_by = models.ForeignKey(User,on_delete=models.CASCADE)
    commented_pin = models.ForeignKey(Pin,on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20,blank=True)
    lastname=models.CharField(max_length=20,blank=True)
    profile_picture = models.ImageField(default="imageplaceholder.jpg", blank=True, upload_to="profilepictures/",)

    def __str__(self):
        return self.user.username



class SavedPins(models.Model):
    pin=models.ForeignKey(Pin,on_delete=models.CASCADE)
    savedby = models.ForeignKey(User, related_name="savedby", on_delete=models.CASCADE)



"""class Topics(models.Model):
    topictitle=models.CharField(max_length=200)"""


"""class Board(models.Model):
    name=models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.CharField(max_length=30,blank=True)"""

