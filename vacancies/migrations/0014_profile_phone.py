# Generated by Django 3.1 on 2020-08-21 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0013_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=375293375940, max_length=32),
            preserve_default=False,
        ),
    ]