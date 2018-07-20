from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from .tasks import send_notification_email

# Create your models here.

class Meme(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    caption = models.CharField(max_length=40,blank=True,null=True)
    image = models.FileField(blank=False,null=False)
    like = models.ManyToManyField(User,blank=True,related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at',]


def meme_post_save(sender, instance, signal, *args, **kwargs):
    print(instance.author.email)
    send_notification_email.delay(instance.author.pk)


signals.post_save.connect(meme_post_save, sender=Meme)

class Comment(models.Model):
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    meme = models.ForeignKey(Meme,related_name='comments',on_delete=models.CASCADE,null=True)