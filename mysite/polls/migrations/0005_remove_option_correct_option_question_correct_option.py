# Generated by Django 4.0.2 on 2022-05-26 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_option_correct_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='correct_option',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_option',
            field=models.CharField(default='hello', max_length=100),
        ),
    ]