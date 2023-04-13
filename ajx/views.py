from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.core import serializers
# Create your views here.
def home(request):
    return render(request,"djangoajx.html")

def upload(request):
    if request.method=="POST":
        image=request.FILES.get("file")
        caption=request.POST.get("caption",False)
        post=Post.objects.create(image=image,caption=caption)
        instance=post.save()
        ser_instance = serializers.serialize('json', [ instance, ])
        return JsonResponse({"instance": ser_instance}, status=200)
    else:
        return render(request,'djangoajx.html')