from django.db import models

# Create your models here.
class Booking(models.Model):
	Advisor = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	date = models.DateField()
	time = models.TimeField()