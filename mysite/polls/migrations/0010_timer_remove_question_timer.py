# Generated by Django 4.0.2 on 2022-05-27 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_alter_question_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timer', models.IntegerField(default=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='timer',
        ),
    ]