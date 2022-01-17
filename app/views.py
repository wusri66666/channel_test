import asyncio

from channels.generic.websocket import JsonWebsocketConsumer
from channels.layers import get_channel_layer
from django.http import QueryDict


class BaseWebsocket(JsonWebsocketConsumer):

    def get_groups(self):
        query_string = self.scope["query_string"]
        query_dict = QueryDict(bytes.decode(query_string))
        groups = [query_dict.get('id')]
        return groups

    @classmethod
    def get_channel_layer(cls):
        return get_channel_layer()

    @classmethod
    def group_send(cls, group, content, close=False):
        channel_layer = cls.get_channel_layer()
        asyncio.run(
            channel_layer.group_send(group, {
                "type": "group.message",
                "content": content,
                "close": close
            })
        )

    def group_message(self, message):
        self.send(text_data=message["content"], close=message["close"])

    def receive(self, text_data=None, bytes_data=None, **kwargs):
        print(text_data)
        self.group_send(self.get_groups()[0], text_data)

    def websocket_connect(self, message):
        self.groups = self.get_groups()
        super(BaseWebsocket, self).websocket_connect(message)
