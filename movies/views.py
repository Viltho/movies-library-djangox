from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movies
from django.urls import reverse_lazy

# Create your views here.
    
class AboutPageView(TemplateView):
    template_name = 'movies/about.html'
    
class MovieListView(ListView):
    template_name = 'movies/movie-list.html'
    model = Movies
    context_object_name = 'movie'

class MovieDetailView(DetailView):
    template_name = 'movies/movie-details.html'
    model = Movies
    
class MovieCreateView(CreateView):
    template_name = 'movies/movie-create.html'
    model = Movies
    fields = ['title','description','user']
    success_url = reverse_lazy("movies_list")
    
class MovieUpdateView(UpdateView):
    template_name = 'movies/movie-update.html'
    model = Movies
    fields = ['title','description','user']
    success_url = reverse_lazy("movies_list")
    
class MovieDeleteView(DeleteView):
    template_name = "movies/movie-delete.html"
    model = Movies
    success_url = reverse_lazy("movies_list")
    