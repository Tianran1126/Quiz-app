# Generated by Django 4.0.2 on 2022-05-26 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_correctoption_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='correct_option',
            field=models.CharField(default='good', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CorrectOption',
        ),
    ]