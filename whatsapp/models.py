from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages")
    receiver = models.ForeignKey(User, related_name="received_messages")
    text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("date published")

    def get_absolute_url(self):
        return "/whatsapp/%i" % self.receiver.id
