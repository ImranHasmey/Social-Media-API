from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
import uuid
# Create your models here.
User = get_user_model()
class Profiles(models.Model):
    email=models.EmailField()
    id_user=models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profileimg=models.ImageField(upload_to='profileimg/',default='blank.jpg')
    bio=models.TextField(blank=True)
    def __str__(self):
        return self.user.username
class Students(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email
class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    img=models.FileField(upload_to='upload/',null=True)
    username=models.CharField(max_length=20)
    caption=models.TextField(max_length=40)
    date=models.DateTimeField(default=datetime.now)
    likes=models.IntegerField(default=0)
    profileimg=models.ImageField(null=True)
    def __str__(self):
        return self.username
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username