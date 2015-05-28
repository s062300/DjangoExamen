from django.db import models

# Create your models here.

class Movie(models.Model):
	movie_name = models.CharField(max_length=50)
	movie_year = models.CharField(max_length=500)
	
	def __unicode__(self):
		return self.movie_name

	
class Acteur(models.Model):
	acteur_name = models.CharField(max_length=300)
	movie_acteur = models.ForeignKey(Movie)

	def __unicode__(self):
		return self.acteur_name