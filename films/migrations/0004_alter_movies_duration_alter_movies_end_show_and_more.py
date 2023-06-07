# Generated by Django 4.2.1 on 2023-05-24 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_rename_id_film_session_film_alter_movies_filf_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='duration',
            field=models.IntegerField(verbose_name='DLITEL'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='end_show',
            field=models.DateField(verbose_name='ENDPROC'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='filf_genre',
            field=models.CharField(max_length=50, verbose_name='ZANR'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='film_description',
            field=models.TextField(default='COOL', max_length=1000, verbose_name='OPIS'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='film_photo',
            field=models.ImageField(upload_to='photos/', verbose_name='PHOTO'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='film_title',
            field=models.CharField(default='LAZANI', max_length=50, verbose_name='NAZV'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='start_show',
            field=models.DateField(verbose_name='НACPROC'),
        ),
        migrations.AlterField(
            model_name='session',
            name='id_room',
            field=models.IntegerField(verbose_name='NUMB'),
        ),
        migrations.AlterField(
            model_name='session',
            name='name_film',
            field=models.CharField(default='LAZANI', max_length=50, verbose_name='NAZ'),
        ),
        migrations.AlterField(
            model_name='session',
            name='price',
            field=models.CharField(max_length=50, verbose_name='PRISE'),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_date',
            field=models.DateTimeField(verbose_name='DATA'),
        ),
    ]