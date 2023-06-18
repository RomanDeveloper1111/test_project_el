from test_project.celery import app
import pytz
from datetime import datetime, time, timedelta
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.models import User
from back.models import Post


@app.task
def check_published_post():
    today = timezone.now().date()
    yesterday = today - timedelta(days=1)

    posts = Post.objects.filter(status='published', published_at__gte=
                                datetime.combine(yesterday, timezone.now().time()),
                                published_at__lt=datetime.combine(today, timezone.now().time()))

    if len(posts) > 0:
        mess_text = ""
        users = User.objects.all()

        now = datetime.utcnow()
        send_time = time(hour=12, minute=0, second=0, microsecond=0)
        for user in users:
            time_zone = pytz.timezone(user.profile.timezone)
            local_now = time_zone.localize(now).time()
            if local_now == send_time:

                for post in posts:
                    mess_text += f'\n{post.author}\n{post.title}\n\n'
                send_mail(
                    'New posts',
                    mess_text,
                    'noreply@example.com',
                    [user.email],
                    fail_silently=False,
                )
