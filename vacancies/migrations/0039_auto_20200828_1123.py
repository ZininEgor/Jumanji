# Generated by Django 3.1 on 2020-08-28 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0038_grademodel_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='grade',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='vacancies.grademodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='vacancies.statusmodel'),
        ),
    ]
