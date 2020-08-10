from django.conf import settings
from django.db import models
from django.utils import timezone

class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    id_vk = models.CharField(max_length=200)
    cooky = models.TextField()
    verify = models.BooleanField(False)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def verify(self):
        pass

    def __str__(self):
        return self.verify

    def add():
        pass