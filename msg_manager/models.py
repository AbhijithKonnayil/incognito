from django.db import models
from django.db.models.fields import EmailField


class Message(models.Model):
    msg = models.CharField(max_length=250)
    email = models.EmailField()
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.msg
