from django.db import models


# Create your models here.
class Foodlog(models.Model):
    title=models.CharField(max_length=200)
    calorie=models.PositiveIntegerField(default=0)
    meal_type=models.CharField(max_length=200)
    serving_size=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    owner=models.CharField(max_length=200)

