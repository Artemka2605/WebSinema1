# Generated by Django 4.2.1 on 2023-06-03 05:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0021_rows_remove_halls_number_seats_remove_halls_rows_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rows',
            options={'verbose_name': 'Ряд', 'verbose_name_plural': 'Ряды'},
        ),
        migrations.AlterModelOptions(
            name='seats',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.RemoveField(
            model_name='halls',
            name='row',
        ),
        migrations.AlterField(
            model_name='movies',
            name='filf_genre',
            field=models.CharField(choices=[('action', 'Боевик'), ('detective', 'Детектив'), ('cartoon', 'Мультфильм'), ('comedy', 'Комедия'), ('documentary', 'Документальный фильм'), ('horror ', 'Ужасы'), ('science_fiction', 'Научная фантастика'), ('criminal_drama', 'Криминальная драма')], default='action', max_length=50, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='rows',
            name='number_row',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Номер ряда'),
        ),
        migrations.AlterField(
            model_name='seats',
            name='number_seat',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Номер места'),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='price',
            field=models.PositiveSmallIntegerField(choices=[('1', '100'), ('2', '150'), ('3', '200'), ('4', '250'), ('5', '300'), ('6', '350'), ('7', '400'), ('8', '450'), ('9', '500')], default='1', verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='films.rows', verbose_name='Ряд'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='films.seats', verbose_name='Место'),
        ),
    ]
