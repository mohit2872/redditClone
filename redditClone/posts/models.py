from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    url = models.TextField()
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=0)
