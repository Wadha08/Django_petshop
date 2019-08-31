from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
	name = models.CharField(max_length=150)
	age = models.IntegerField()
	available = models.BooleanField(default=True)
	image = models.ImageField(null=True)
	price = models.DecimalField(max_digits=10, decimal_places=3)
