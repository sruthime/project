# Generated by Django 4.2.3 on 2023-12-13 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_appointment_bookeddate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Departmentt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.departments'),
        ),
    ]
