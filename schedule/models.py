from django.db import models


class Timetable(models.Model):
    timetable_date = models.DateField(auto_now_add=False, auto_now=False)
    timetable_start = models.TimeField(auto_now_add=False, auto_now=False)
    timetable_name_of_class = models.CharField(max_length=50)
    timetable_idea_of_class = models.TextField()