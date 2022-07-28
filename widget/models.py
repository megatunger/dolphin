from django.db import models
from django.contrib.auth.models import User

class Widget(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=1024)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class ScalarToken(models.Model):
    userId = models.CharField(max_length=200)
    scalarToken = models.CharField(max_length=200, db_index=True)
    sytToken = models.CharField(max_length=200, db_index=True)
