from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    if request.method == "POST":
        task = request.POST.get('task')
        Task.objects.create(task=task)
    return redirect('home')
    # return render(request, 'addTask.html')

def mark_as_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        new_task = request.POST.get('task')
        task.task = new_task
        task.save()
        return redirect('home')
    context = {
        'task': task
    }
    return render(request, 'edit_task.html', context)

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')