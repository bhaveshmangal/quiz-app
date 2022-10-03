from channels.generic.websocket import AsyncJsonWebsocketConsumer
from quiz import settings
import json

class QuizConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.test_date = self.scope["url_route"]["kwargs"]["test_date"]
        self.room_group_name = 'test_%s' % self.test_date

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )
        await super().disconnect(code)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))