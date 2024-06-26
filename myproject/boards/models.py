from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Topic(models.Model):
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    starter = models.ForeignKey('auth.User', related_name='topics', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class Post(models.Model):
    message = models.TextField()
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('auth.User', null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.message[:30]
