from src.celery_utils.celery_app import celery

@celery.task(name="celery_utils.tasks.print_hello")
def print_hello():
    print("Hello from Celery!")
