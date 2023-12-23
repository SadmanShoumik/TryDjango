from django.db import models

# Create your models here.
class Product(models.Model):
	title       = models.CharField(max_length=120) #max_length is required for CharField 
	description = models.TextField(blank=True, null=True) 
	price       = models.DecimalField(decimal_places=2, max_digits=10000)
	summary     = models.TextField(blank=False, null=True) # blank has nothing to do with the database, only the textbox, null deals with the database 
	featured    = models.BooleanField() # null=True OR default=True OR default=False

