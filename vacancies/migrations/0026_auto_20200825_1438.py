# Generated by Django 3.1 on 2020-08-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0025_auto_20200825_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='employee_count',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]