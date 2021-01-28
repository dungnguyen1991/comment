from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Comment(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    content     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    comment     = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
