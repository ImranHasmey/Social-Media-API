from django.shortcuts import render,HttpResponse,redirect
import mysql.connector
from .models import Blog
from django.http import JsonResponse
from django.core import serializers
from .forms import ParticipantForm
from .models import Participant

def ord(request):
    return render(request,"register.html")
def home(request):
    post=Blog.objects.all()
    return render(request,'result.html',{'post':post})
def hello(request):
    return render(request,'home.html')
def add(request):
    return render(request,'post.html')
def sub(request):
    v1=request.POST['num1']
    v2=request.POST['num2']
    res=int(v1)-int(v2)
    return render(request,"result.html",{"result":res})
def verify(request):
    username=request.POST['num1']
    password=request.POST['num2']
    result=""
    try:
        
        connection=mysql.connector.connect(host="localhost",database="sample",user="root",password="8309343286")
        cursor=connection.cursor()
        cursor.execute("select name,age from users")
        res=cursor.fetchall()
        for i in res:
            if username in i and password in i:
                result="User Already Registerd"
        if result=="":
            result="User Not Registerd"
        return render(request,"result.html",{"result":result})
    except Exception:
        pass
def inserting(request):
    username=request.POST['num1']
    password=int(request.POST['num2'])
    result="success"
    try:
        conn=mysql.connector.connect(host="localhost",database="sample",user="root",password="8309343286")
        cursor=conn.cursor()
        s1="""insert into user(name,age) values(%s,%s)"""
        s2=(username,password)
        cursor.execute(s1,s2)
        cursor.commit()
        return render(request,"result.html",{"result":result})
    except Exception:
        pass
def blog(request):
    if request.method=='POST':
        title=request.POST['title']
        img=request.FILES.get('image')
        blog=Blog(title=title,image=img)
        blog.save()
        return render(request,'post.html')
    else:
        return render(request,'post.html')

def displayData(request):
    form = ParticipantForm()
    participants = Participant.objects.all()
    return render(request, "index.html", {"form": form, "participants": participants})

def postParticipant(request):
    # request should be ajax and method should be POST.
    if  request.method == "POST":
        # get the form data
        form = ParticipantForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new participant object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'  




