# Generated by Django 3.1 on 2020-08-14 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0004_auto_20200814_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campanies', to='vacancies.company'),
        ),
    ]
