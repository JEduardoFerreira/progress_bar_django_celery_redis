from django.shortcuts import render

from .tasks import go_to_sleep


def index(request):
    go_to_sleep.apply_async(args=[5])
    return render(request, 'html/index.html')