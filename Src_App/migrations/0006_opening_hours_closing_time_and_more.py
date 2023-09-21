# Generated by Django 4.1.7 on 2023-09-07 04:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0005_alter_opening_hours_last_modified_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opening_hours',
            name='closing_time',
            field=models.CharField(choices=[('1 AM', '1 AM'), ('2 AM', '2 AM'), ('3 AM', '3 AM'), ('4 AM', '4 AM'), ('5 AM', '5 AM'), ('6 AM', '6 AM'), ('7 AM', '7 AM'), ('8 AM', '8 AM'), ('9 AM', '9 AM'), ('10 AM', '10 AM'), ('11 AM', '11 AM'), ('12 AM', '12 AM'), ('1 PM', '1 PM'), ('2 PM', '2 PM'), ('3 PM', '3 PM'), ('4 PM', '4 PM'), ('5 PM', '5 PM'), ('6 PM', '6 PM'), ('7 PM', '7 PM'), ('8 PM', '8 PM'), ('9 PM', '9 PM'), ('10 PM', '10 PM'), ('11 PM', '11 PM'), ('12 PM', '12 PM')], max_length=50, null=True, verbose_name='Closing Time'),
        ),
        migrations.AlterField(
            model_name='opening_hours',
            name='last_modified_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 7, 9, 47, 13, 34669), verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='opening_hours',
            name='opening_time',
            field=models.CharField(choices=[('1 AM', '1 AM'), ('2 AM', '2 AM'), ('3 AM', '3 AM'), ('4 AM', '4 AM'), ('5 AM', '5 AM'), ('6 AM', '6 AM'), ('7 AM', '7 AM'), ('8 AM', '8 AM'), ('9 AM', '9 AM'), ('10 AM', '10 AM'), ('11 AM', '11 AM'), ('12 AM', '12 AM'), ('1 PM', '1 PM'), ('2 PM', '2 PM'), ('3 PM', '3 PM'), ('4 PM', '4 PM'), ('5 PM', '5 PM'), ('6 PM', '6 PM'), ('7 PM', '7 PM'), ('8 PM', '8 PM'), ('9 PM', '9 PM'), ('10 PM', '10 PM'), ('11 PM', '11 PM'), ('12 PM', '12 PM')], max_length=50, verbose_name='Opening Time'),
        ),
        migrations.AlterField(
            model_name='used_car',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 7, 9, 47, 13, 33670), verbose_name='Last Edited on'),
        ),
    ]
