# Generated by Django 4.0.2 on 2022-05-29 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_delete_correct_question_selected_option_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Timer',
        ),
    ]
