from django.db import models
from django.contrib.auth.models import User


class Creator(models.Model):
    PLATFORM_CHOICES = (
        ('instagram', 'Instagram'),
        ('tiktok', 'TikTok'),
        ('user generated content', 'User Generated Content')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    platform = models.CharField(max_length=22, choices=PLATFORM_CHOICES)

    def __str__(self):
        return self.user.get_full_name()


class Content(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f'Created by {self.user}'
