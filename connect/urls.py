from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.main,name='main'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('imgupload',views.imgupload,name='imgupload'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like_post', views.like_post, name='like_post'),
    path('homepage',views.homepage,name='homepage')
]