import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "producer_consumer.settings")

app = Celery("producer_consumer")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "make order (every 1 minute)": {
        "task": "order_app.tasks.make_order",
        "schedule": crontab(minute="*/1"),
    },
}
