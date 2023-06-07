# Generated by Django 4.2.1 on 2023-05-21 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_film', models.CharField(default='Лазанья', max_length=50, verbose_name='Название')),
                ('id_room', models.IntegerField(verbose_name='Номер зала')),
                ('start_date', models.DateTimeField(verbose_name='Дата')),
                ('price', models.CharField(max_length=50, verbose_name='Цена билета')),
                ('id_film', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='films.movies')),
            ],
        ),
    ]
