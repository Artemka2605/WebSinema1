# Generated by Django 4.2.1 on 2023-06-06 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0030_alter_seats_options_alter_sessions_options_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seats',
            unique_together={('number_seat', 'number_row', 'session')},
        ),
    ]
