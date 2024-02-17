from channels.layers import get_channel_layer
from asgi_http.responses import JSONResponse

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.channel_layer.group_add("chatroom", self.channel_name)
        await self.send_json({"message": "You connected!"})

    async def websocket_receive(self, event):
        message = event["text"]
        await self.channel_layer.group_send(
            "chatroom", {"type": "chat.message", "message": message}
        )

    async def chat_message(self, event):
        message = event["message"]
        await self.send_json({"message": message})

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard("chatroom", self.channel_name)
