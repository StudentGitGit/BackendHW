from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_movies),
    path('<int:movie_id>/', views.get_movie_by_id),
]
