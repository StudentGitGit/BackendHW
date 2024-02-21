from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

def todo_lists(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'todos/todo_lists.html', {'todo_lists': todo_lists})

def todo_list_details(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = todo_list.todo_set.all()
    return render(request, 'todos/todo_list_details.html', {'todo_list': todo_list, 'todos': todos})

def todo_list_create(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm()
    return render(request, 'todos/todo_list_create.html', {'form': form})

def todo_create(request, list_id):
    todo_list = get_object_or_404(TodoList, id=list_id)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list
            todo.save()
            return redirect('todo_list_details', id=list_id)
    else:
        form = TodoForm()
    return render(request, 'todos/todo_create.html', {'form': form})
