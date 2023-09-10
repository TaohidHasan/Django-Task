from django.db import models

class Stock(models.Model):  
	date = models.DateField()
	Trade = models.CharField(max_length=255)  
	High = models.FloatField(max_length=255)
	Low = models.FloatField(max_length=255)
	Open = models.FloatField(max_length=255)
	Close = models.FloatField(max_length=255)
	Volume = models.IntegerField() 
	def __str__(self):
		return self.Trade  

	class Meta:  
		db_table = "stocklist"
		ordering = ['date'] 