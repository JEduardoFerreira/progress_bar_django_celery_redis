from celery import shared_task
from celery_progress.backend import ProgressRecorder
from time import sleep

@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress = ProgressRecorder(self)
    r = 5
    for i in range(r):
        sleep(duration)
        progress.set_progress(i+1, 5, f'{i+1} de {r} iterações concluídas.')
    return 'Terminou!'