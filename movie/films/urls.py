from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
	#url(r'^specifics/(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<movie_id>[0-9]+)/results/$', views.results, name='results'),
]