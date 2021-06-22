from django.db import models

class Actor(models.Model):
	first_name      = models.CharField(max_length=45)
	last_name       = models.CharField(max_length=45)
	date_of_birth   = models.DateField()

	class Meta:
		db_table = 'actors'

class Movie(models.Model):
	title           = models.CharField(max_length=45)
	release_date    = models.DateField()
	running_time    = models.IntegerField()
	actors		= models.ManyToManyField(Actor, related_name='movies')

	class Meta:
		db_table = 'movies'
