from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    tags = models.CharField(max_length=30)
    createdAt = models.DateTimeField(auto_now_add=True) ## Set when object is created
    updatedAt = models.DateTimeField(auto_now=True)     ## Set every time object is updated
