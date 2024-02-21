from django.urls import path
from . import views

urlpatterns = [
    path('todo-lists/', views.todo_lists, name='todo_lists'),
    path('create/', views.todo_list_create, name='todo-list-create'),
    path('<int:id>/', views.todo_list_details, name='todo-list-details'),
    path('<int:list_id>/todos/create/', views.todo_create, name='todo-create'),
]
