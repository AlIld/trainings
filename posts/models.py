from django.db import models
from user.models import New_user


class Post(models.Model):
    post_topic = models.TextField()
    post_text = models.TextField()
    post_author = models.ForeignKey(New_user, on_delete=models.CASCADE, related_name='author')
    post_date_creating = models.DateTimeField(auto_now_add=True)
    post_likes = models.IntegerField(default=0)

class Comments(models.Model):
    comments_text = models.TextField()
    comments_post = models.ForeignKey(Post, on_delete=models.CASCADE)
