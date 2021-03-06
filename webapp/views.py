
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from webapp.models import STATUS_CHOICES, Task



def index_view(request):
    return render(request, 'index.html')


def create_task(request):
    if request.method == "GET":
        context = {'status1': STATUS_CHOICES}
        return render(request, "create.html", context)
    else:
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")
        date = request.POST.get("date")
        new_task = Task.objects.create(description=description, status=status, date=date, title=title)
        # context = {"new_task": new_task}
        print(new_task.pk)
        return redirect("task_view", pk=new_task.pk)


def tasks_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks_view.html', context)


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task': task
    }
    return render(request, 'task_view.html', context)
