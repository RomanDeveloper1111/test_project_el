from celery import Celery

from celery.schedules import crontab
from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings.settings")
app = Celery('test_project')

app.config_from_object('django.conf:settings', namespace="CELERY")
app.conf.broker_url = settings.REDIS_URL
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'notification_new_posts': {
        'task': 'back.tasks.check_published_post',
        'schedule': crontab(),
    },


}