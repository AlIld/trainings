from django.db import models
from user.models import New_user


class New_chat(models.Model):
    chat_text = models.TextField()
    chat_sender = models.ForeignKey(New_user, on_delete=models.CASCADE, related_name='sender')
    chat_recipient = models.ForeignKey(New_user, on_delete=models.CASCADE, related_name='recipient')
    chat_date = models.DateTimeField(auto_now_add=True)