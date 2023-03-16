from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Author

User = get_user_model()


class Tweet(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_add = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def str(self):
        return f'{self.author.name} - {self.title}'


class Message(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    chat = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.chat} - {self.author.name}'





