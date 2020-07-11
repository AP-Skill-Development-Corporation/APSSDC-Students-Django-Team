from django.db import models

# Create your models here.
class Change(models.Model):
	name=models.CharField(max_length=50)
	username=models.CharField(max_length=50)
	mailid=models.EmailField(max_length=50)
	password=models.CharField(max_length=20)
	mobile=models.IntegerField(null=True)


