from django.contrib import admin

# Register your models here.

from .models import Acteur, Movie

class ActeurInline(admin.TabularInline):
    model = Acteur
    extra = 3

class MovieAdmin(admin.ModelAdmin):
	fields = ['movie_name', 'movie_year']
	inlines = [ActeurInline]
	list_display = ('movie_name', 'movie_year')

admin.site.register(Movie, MovieAdmin)