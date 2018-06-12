from django.db import models
class User(models.Model):
    Username=models.CharField(max_length=30)
    PassWord=models.CharField(max_length=30)
    def __str__(self):
        return self.Username
# Create your models here.
