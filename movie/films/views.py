from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.http import HttpResponse


from .models import Movie

# Create your views here.
	
def index(request):
    latest_movie_list = Movie.objects.order_by('-movie_year')[:5]
    context = {'latest_movie_list': latest_movie_list}
    return render(request, 'films/index.html', context)

def detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'films/detail.html', {'movie': movie})

def results(request, movie_id):
    response = "You're looking at the results of movie %s."
    return HttpResponse(response % movie_id)
