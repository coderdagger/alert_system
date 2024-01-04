from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import telegram
import json
import traceback


class SendMessage(APIView):
    permission_classes = []

    def post(self, request):
        try:
            message = json.loads(request.body).get('message')
            bot = telegram.Bot(token=settings.TELEGRAM['bot_token'])
            bot.send_message(chat_id=settings.TELEGRAM['channel_name'], text=message)
            return Response("Successfully sent the message to telegram.")
        except:
            traceback.print_exc()
            return Response("Failed to send the telegram message.")
