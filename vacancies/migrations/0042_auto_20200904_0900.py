# Generated by Django 3.1 on 2020-09-04 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0041_auto_20200902_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.CharField(max_length=32),
        ),
    ]
