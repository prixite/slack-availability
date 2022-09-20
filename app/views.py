from django.shortcuts import render

from slack_bolt.adapter.django import SlackRequestHandler

from django.views.decorators.csrf import csrf_exempt

from app.slack_listeners import app

handler = SlackRequestHandler(app=app)

@csrf_exempt
def slack_events_handler(request):
    return handler.handle(request)
