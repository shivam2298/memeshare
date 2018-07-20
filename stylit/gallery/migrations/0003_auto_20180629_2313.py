# Generated by Django 2.0.4 on 2018-06-29 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180629_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meme',
            name='image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='meme',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
