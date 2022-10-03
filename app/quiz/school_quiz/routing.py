from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(
        "ws/test/(?<test_date>[0-9-]+)/",
        consumers.QuizConsumer.as_asgi(),
    ),
]