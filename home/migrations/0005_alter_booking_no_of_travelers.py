# Generated by Django 3.2.3 on 2021-06-17 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_traveler_booking_no_of_travelers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_travelers',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]