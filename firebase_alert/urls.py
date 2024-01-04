from .views import  * 
from django.contrib import admin
from django.urls import path

app_name='firebase_alert'

urlpatterns = [
    path('push-notification/', PushNotification.as_view()),
    path('home', index),
    path('send', send)
]
