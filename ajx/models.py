from django.db import models

# Create your models here.
class Post(models.Model):
    image=models.FileField(null=True)
    caption=models.TextField(max_length=20)


