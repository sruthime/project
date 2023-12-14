# Generated by Django 4.2.3 on 2023-12-13 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_faculty_fdept_remove_faculty_fimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=200)),
                ('aemail', models.EmailField(max_length=200)),
                ('bookeddate', models.DateField(auto_now=True)),
                ('facname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.faculty')),
            ],
        ),
    ]