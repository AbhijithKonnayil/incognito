
from django.urls import path
from .views import view_msg, SendMessage
urlpatterns = [
    path('', SendMessage.as_view(), name='send_message'),
    path('view/', view_msg, name='view_message'),
]
