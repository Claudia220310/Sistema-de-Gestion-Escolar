# Generated by Django 5.0.6 on 2024-06-21 16:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0006_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='student',
            name='registration_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]