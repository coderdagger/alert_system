from firebase_alert.views import PushNotification
from .views import  * 
from django.contrib import admin
from django.urls import path, include
from firebase_alert.views import firebaseserviceworker

urlpatterns = [
    path('firebase/', include('firebase_alert.urls')),
    path('admin/', admin.site.urls),
    path('send_message', SendMessage.as_view()),
    path('firebase-messaging-sw.js', firebaseserviceworker),
]
