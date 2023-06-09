# Generated by Django 4.2.1 on 2023-05-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_title', models.CharField(default='Лазанья', max_length=50, verbose_name='Название')),
                ('filf_genre', models.CharField(max_length=50, verbose_name='Жарн')),
                ('film_description', models.TextField(default='Этот фильм удивит вас', max_length=1000, verbose_name='Описание')),
                ('film_photo', models.ImageField(upload_to='photos/', verbose_name='Фото')),
                ('duration', models.IntegerField(verbose_name='Длительность')),
                ('start_show', models.DateField(verbose_name='Начало проката')),
                ('end_show', models.DateField(verbose_name='Конец проката')),
                ('in_cinemas', models.BooleanField(default=False)),
            ],
        ),
    ]
