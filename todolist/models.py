from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=32)
    details = models.CharField(max_length=32)
