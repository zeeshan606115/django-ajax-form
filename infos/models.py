from django.db import models

# Create your models here.

class Info(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.name)