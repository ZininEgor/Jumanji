# Generated by Django 3.1 on 2020-09-04 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0042_auto_20200904_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.CharField(max_length=124),
        ),
    ]