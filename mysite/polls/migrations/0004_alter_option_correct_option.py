# Generated by Django 4.0.2 on 2022-05-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_option_correct_option_delete_correctoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='correct_option',
            field=models.CharField(default='hello', max_length=100),
        ),
    ]
