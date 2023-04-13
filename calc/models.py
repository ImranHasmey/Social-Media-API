from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to="profile_images/")
    createdat=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title
class Participant(models.Model):
    # participant form fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length = 250)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    city = models.CharField(max_length=150)
