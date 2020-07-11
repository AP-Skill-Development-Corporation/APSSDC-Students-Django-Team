from django.db import models

# Create your models here.
class Movies(models.Model):
	hero=models.CharField(max_length=50)
	heroien=models.CharField(max_length=50)
	director=models.CharField(max_length=20)
	producer=models.CharField(max_length=20)
	budget=models.IntegerField(null=True)
	reldate=models.DateField(null=True)