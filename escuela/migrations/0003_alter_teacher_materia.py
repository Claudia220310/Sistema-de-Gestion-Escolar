# Generated by Django 5.0.6 on 2024-06-18 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0002_teacher_materia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='materia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
