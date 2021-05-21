from django.db import models

# Create your models here.

class Post(models.Model):
	Name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='image/')


