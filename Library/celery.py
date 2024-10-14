from celery import Celery
import os 

os.environ.setdefault("DJANGO_SETTING_MODULE", "Library.settings")

app = Celery("book_store")


app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()