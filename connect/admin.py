from django.contrib import admin
from .models import Profiles,Students,Post,LikePost
# Register your models here.

admin.site.register(Profiles)
admin.site.register(Students)
admin.site.register(Post)
admin.site.register(LikePost)