from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_articles, name='article_list'),
    path('<int:article_id>/', views.get_article_by_id, name='article_detail'),
]
