from django.core.validators import FileExtensionValidator
from django.db import models
from accounts.models import UserProfile
# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(blank=True, null=True)
    vote_post = models.ManyToManyField(User, blank=True, related_name='votes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts')


    def __str__(self):
        return self.title



class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='posts')
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{self.body}"


VOTE_CHOICES = (
    ('upvote', 'upvote'),
    ('downvote', 'downvote'),
)


class Vote(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=VOTE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"
