from django.urls import path, include
from .views import (
    AboutPageView,
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieDeleteView,
    MovieUpdateView
    )

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about_page'),
    path('', MovieListView.as_view(), name='movies_list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movies_detail'),
    path('create/', MovieCreateView.as_view(), name='movies_create'),
    path('<int:pk>/update/', MovieUpdateView.as_view(), name='movies_update'),
    path('<int:pk>/delete/', MovieDeleteView.as_view(), name='movies_delete'),
]