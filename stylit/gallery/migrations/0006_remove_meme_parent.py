# Generated by Django 2.0.4 on 2018-07-19 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20180705_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meme',
            name='parent',
        ),
    ]
