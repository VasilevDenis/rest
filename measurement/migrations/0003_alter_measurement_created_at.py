# Generated by Django 4.2.4 on 2023-08-31 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_measurement_sensor_alter_measurement_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
