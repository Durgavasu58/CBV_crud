from django.db import models

# Create your models here.

class Student(models.Model):
	rollno=models.IntegerField(default=False)
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=1000)
	city=models.CharField(max_length=100)
	marks=models.IntegerField()

	def __str__(self):
		return self.name

