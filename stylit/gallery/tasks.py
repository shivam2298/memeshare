from django.core.mail import send_mail
import logging

from django.contrib.auth.models import User
from django.core.mail import send_mail

from stylit.celery import app


@app.task
def send_notification_email(user_id):
    user = User.objects.get(pk=user_id)

    for f in user.followers.all():
        print(f.user.email)
        send_mail(
            'A new post',
            user.username+' created a new post ,check it out',
            'shivamrustagi@hotmail.com',
            [f.user.email],
            fail_silently=False,
        )

