from django.shortcuts import render

from .tasks import go_to_sleep


def index(request):
    task = go_to_sleep.apply_async(args=[5])
    print(task)
    #task.get()
    return render(request, 'html/index.html')