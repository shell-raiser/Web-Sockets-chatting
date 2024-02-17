from chat.consumers import ChatConsumer
from channels.routing import ProtocolTypeRouter, ChannelNameRouter

channel_routing = [
    ProtocolTypeRouter({
        "websocket": ChannelNameRouter({"chat": ChatConsumer}),
    }),
]
