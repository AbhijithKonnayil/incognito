from django.db import models
from django.db.models.fields import EmailField
from django.conf import settings


class Message(models.Model):
    msg = models.CharField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.msg
