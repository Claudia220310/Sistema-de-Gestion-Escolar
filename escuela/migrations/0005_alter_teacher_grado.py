# Generated by Django 5.0.6 on 2024-06-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0004_remove_teacher_materia_teacher_grado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='grado',
            field=models.CharField(max_length=30),
        ),
    ]
