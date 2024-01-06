import json
from urllib.request import Request
import requests
from django.http import HttpResponse
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import firebase_admin
from firebase_admin import credentials, messaging
from django.conf import settings
from django.shortcuts import render
import webbrowser



def index(request):
    if request.method  == 'GET':
        return render(request, 'index.html')

credentials_path = os.path.join(settings.BASE_DIR, 'firebase_alert', 'credentials.json')

# Initialize Firebase Admin SDK
cred = credentials.Certificate(credentials_path)
firebase_admin.initialize_app(cred)

class PushNotification(APIView):
    def post(self, request, *args, **kwargs):
        # Assuming your request data contains the FCM token and notification message
        fcm_token = request.data.get('fcm_token')
        message = request.data.get('message')
        print(fcm_token)
        print(message)

        if not fcm_token or not message:
            return Response({"error": "FCM token and message are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Send push notification
        try:
            registration_token = fcm_token
            notification = messaging.Notification(
                title='Your Notification Title',
                body=message,
            )
            message = messaging.Message(
                notification=notification,
                token=registration_token,
            )
            response = messaging.send(message)

            webbrowser.open(request.build_absolute_uri(location='/static/iphone_sound.mp3'))
            webbrowser.open(request.build_absolute_uri(location='/firebase/home'))
            return Response({"success": "Push notification sent successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"Failed to send push notification: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def firebaseserviceworker(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.6.3/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.6.3/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyDLbzUWn2XYjtWS8aV-vLuI-GnVGhnHXWU",' \
         '        authDomain: "upworkproject-585da.firebaseapp.com",' \
         '        projectId: "upworkproject-585da",' \
         '        storageBucket: "upworkproject-585da.appspot.com",' \
         '        messagingSenderId: "407386294372",' \
         '        appId: "1:407386294372:web:1f93ed2c4c4d2d50a9f771",' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.onBackgroundMessage(function (payload) {' \
         '    console.log(payload);' \
         '    console.log(payload.notification.body);' \
         '    const audio=new Audio("/static/iphone_sound.mp3");' \
         '    audio.play();' \
         '    const notificationOption={' \
         '        body:payload.notification.body' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")


def send_notification(registration_ids , message_title , message_desc):
    # Assuming your request data contains the FCM token and notification message
        fcm_token = 'etWEBdAz8005mPYG0jN7BA:APA91bHcaByboxLSkp2FV-46VsinlfG2E7oyvG7razYkna5GwKun4JXiesMjVgTShWSs1x8gba-NEyGdZvhCKNKzs1KNdmvKLKKjZYazlkDHNNNuU4WbuuaFEcy277jz54iKre6ako-f'
        message = 'testing_firebase'
        print(fcm_token)
        print(message)

        if not fcm_token or not message:
            return Response({"error": "FCM token and message are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Send push notification
        registration_token = fcm_token
        notification = messaging.Notification(
            title='Your Notification Title',
            body=message,
        )
        message = messaging.Message(
            notification=notification,
            token=registration_token,
        )
        response = messaging.send(message)
        print(response)


def send(request):
    resgistration  = ['etWEBdAz8005mPYG0jN7BA:APA91bHcaByboxLSkp2FV-46VsinlfG2E7oyvG7razYkna5GwKun4JXiesMjVgTShWSs1x8gba-NEyGdZvhCKNKzs1KNdmvKLKKjZYazlkDHNNNuU4WbuuaFEcy277jz54iKre6ako-f']
    send_notification(resgistration , 'Code Keen added a new video' , 'Code Keen new video alert')
    return HttpResponse("sent")