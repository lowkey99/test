
from django.db import models


class events(models.Model):
    events_title = models.CharField(max_length=30)
    events_disc = models.CharField(max_length=600)
    profile = models.ImageField(null=True,blank=True)
    time =  models.DateTimeField(auto_now_add=True)
