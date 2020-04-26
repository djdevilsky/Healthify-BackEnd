from django.db import models
# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Doctor(models.Model):
    name = models.CharField(max_length=60)
    imageURL = models.CharField(max_length=600)
    experience = models.FloatField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)

