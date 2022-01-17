from django.conf.urls import url
from app.views import *

websocket_urlpatterns = [
    url(r'^ws/msg/', BaseWebsocket),
]