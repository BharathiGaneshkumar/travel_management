# Generated by Django 3.2.3 on 2021-06-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210617_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District', models.CharField(max_length=20)),
            ],
        ),
    ]