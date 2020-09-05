# Generated by Django 2.2 on 2020-09-03 11:05

from django.db import migrations, models
import django.db.models.deletion
import doctor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='images/')),
                ('department', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10, validators=[doctor.models.validate_day])),
                ('start_time', models.CharField(max_length=2, validators=[doctor.models.validate_hour])),
                ('end_time', models.CharField(max_length=2, validators=[doctor.models.validate_hour])),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.DoctorInfo')),
            ],
        ),
    ]