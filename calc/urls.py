from django.urls import path,include
from . import views
from .views import (
    displayData,
    postParticipant, 
)
urlpatterns = [
    path('', displayData),
    path('participant', postParticipant, name = "post_participant"),

]
