from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Use to write SQL code (Abstraction through ORM)
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # Cascades when user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE) 