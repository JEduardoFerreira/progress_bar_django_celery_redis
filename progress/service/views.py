from django.shortcuts import render
from .tasks import go_to_sleep


def index(request):
    task = go_to_sleep.delay(10)
    return render(request, 'html/index.html', context={'task_id' : task.task_id})