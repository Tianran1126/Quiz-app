# Generated by Django 4.0.2 on 2022-05-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='timer',
            field=models.IntegerField(default=0),
        ),
    ]
