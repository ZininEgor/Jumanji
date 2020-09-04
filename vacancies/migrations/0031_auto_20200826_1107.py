# Generated by Django 3.1 on 2020-08-26 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0030_auto_20200825_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='vacancies.vacancy'),
        ),
    ]