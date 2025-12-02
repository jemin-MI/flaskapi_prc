from celery import Celery


def make_celery():
    celery_main = Celery(
        'celery_example',
        broker='redis://localhost:6379/0',
        backend='redis://localhost:6379/0',
        include = ['src.celery_utils.tasks']
    )

    celery_main.conf.beat_schedule = {
        "print-hello-every-4-seconds": {
            "task": "celery_utils.tasks.print_hello",
            "schedule": 4.0,
        }
    }

    return celery_main


celery = make_celery()
