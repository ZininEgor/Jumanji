# Generated by Django 3.1 on 2020-08-28 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0035_auto_20200828_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='specialty',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='vacancies.specialty'),
            preserve_default=False,
        ),
    ]
