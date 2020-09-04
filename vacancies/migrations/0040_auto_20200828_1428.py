# Generated by Django 3.1 on 2020-08-28 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0039_auto_20200828_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='vacancies.grademodel'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='specialty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='vacancies.specialty'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='vacancies.statusmodel'),
        ),
    ]
