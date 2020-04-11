from django.db import models
from schedule.models import Timetable
from user.models import New_user
from posts.models import Post


class Group(models.Model):
    group_users = models.ForeignKey(New_user, on_delete=models.CASCADE, blank=True)
    group_name = models.CharField(max_length=25)
    group_post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True)
    group_timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, blank=True)
    # group_stars = models.TextField()
