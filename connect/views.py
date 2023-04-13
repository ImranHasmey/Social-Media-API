from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Profiles,Students,Post,LikePost
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
        if request.method == 'POST':   
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']
            res=request.POST['res']
            if res=='ok':    
                if Students.objects.filter(email=email).exists():
                    if User.objects.filter(email=email).exists():
                        messages.info(request,'Email Already Existed')
                        return redirect('register')
                    elif User.objects.filter(username=username).exists():
                        messages.info(request,'Username Taken')
                        return redirect('register')
                    else:
                        user=User.objects.create_user(email=email,username=username,password=password)
                        user.save()
                        user_model= User.objects.get(username=username)
                        new_profile = Profiles.objects.create(user=user_model,id_user=user_model.id)
                        new_profile.save()
                    messages.info(request,'Succesfully Registerd')
                    return redirect('login')
                else:
                    messages.info(request,"you are not a registered student")
                    return redirect('register')
            else:
                return redirect('register')
        else:
            return render(request,'register.html')
@login_required(login_url='home')
def logout(request):
    auth.logout(request)
    return redirect('home')
@login_required(login_url='home')
def imgupload(request):
    if request.method=='POST':
        img=request.FILES.get('image')
        username=request.user.username
        caption=request.POST['caption']
        profile=Profiles.objects.get(user=request.user)
        p=Post.objects.create(img=img,username=username,caption=caption,profileimg=profile.profileimg)
        p.save()
        return redirect('/')
    else:
        post=Post.objects.all()
        return redirect('/')
@login_required(login_url='home')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.likes = post.likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.likes = post.likes-1
        post.save()
        return redirect('/')
@login_required(login_url='home')
def profile(request,pk):
    username=request.user.username
    user_object = User.objects.get(username=pk)
    user_profile = Profiles.objects.get(user=user_object)
    user_posts = Post.objects.filter(username=pk)
    post_length = len(user_posts)
    return render(request,'profile.html',{'user_profile':user_profile,'user_posts':user_posts,'post_length':post_length})
@login_required(login_url='home')
def main(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profiles.objects.get(user=user_object)
    post=Post.objects.all()
    temp=[]
    for i in post:
        temp.append(i)
    t=temp[::-1]
    return render(request,'main.html',{'user_profile':user_profile,'post':t})
@login_required(login_url='home')
def homepage(request):
    return redirect('/')
        