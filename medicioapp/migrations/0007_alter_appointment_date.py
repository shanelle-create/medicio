# Generated by Django 5.0.6 on 2024-07-10 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicioapp', '0006_rename_name_appointment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(max_length=10),
        ),
    ]