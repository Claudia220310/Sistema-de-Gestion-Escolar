# Generated by Django 5.0.6 on 2024-06-27 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0012_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('Presente', 'Presente'), ('Ausente', 'Ausente'), ('Tardanza', 'Tardanza')], max_length=10),
        ),
    ]
