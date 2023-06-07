import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



############################################validate##############################3
def validate_even(start_time, end_time):
    if start_time >= end_time:
        raise ValidationError(
            _('Проверьте время окончания, оно не может быть меньше времени начала '),
            params={'start_time': start_time, 'end_time': end_time},
        )

    t = Sessions.objects.all()
    #print(t)
    time_sesstion = t.filter(start_time__lte=start_time).filter(end_time__gte=start_time) # время между сеансами
    #print(time_sesstion)
    if time_sesstion:
        raise ValidationError('Проверьте, чтобы предыдущий сеанс завершился')


def validate_unique(SEAT_id, SESSION_id):

    k = Tickets.objects.filter(seat_id=SEAT_id, session_id=SESSION_id).exists()
    if k:
        raise ValidationError('Запись с такими местом и сеансом уже существует ')
    #
    #
    # #print(t)
    # time_sesstion = t.filter(start_time__lte=start_time).filter(end_time__gte=start_time) # время между сеансами
    # #print(time_sesstion)
    # if time_sesstion:
    #     raise ValidationError('Проверьте, чтобы предыдущий сеанс завершился')


# def validate_phone_number(phone_number):
#     if len(  str(phone_number)) < 11 or len( str( phone_number)) > 11:
#         raise ValidationError('Неверный формат номера телефона')




class Sessions(models.Model):

    PRICE_CHOICES = (
        ('100', '100'),
        ('150', '150'),
        ('200', '200'),
        ('250', '250'),
        ('300', '300'),
        ('350', '350'),
        ('400', '400'),
        ('450', '450'),
        ('500', '500'),
    )

    start_time = models.DateTimeField('Время начала')
    end_time = models.DateTimeField('Время окончания') #validators=)
    price = models.CharField(verbose_name='Цена', choices=PRICE_CHOICES, max_length=10, default='100')
    film = models.ForeignKey('Movies', on_delete=models.PROTECT, verbose_name='Фильм')  # Movies - название таблицы (класса в файле models)


    def __str__(self):
        dat = str(self.start_time + datetime.timedelta(hours=7)) # прибавка к дате
        return str(f'{self.film} {dat[:-6]}')    # отрезали конец
        #str(f' {str(self.film)} {str(self.start_date)}')

    class Meta:  # название табл. в админке (ед. и мн. числа)
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'
        unique_together = ('start_time', 'film')
        ordering = ['start_time', ]

    def clean(self):
        validate_even(self.start_time,self.end_time)



class Movies(models.Model):

    GENRE_CHOICES = (
        ('Боевик', 'Боевик'),
        ('Детектив', 'Детектив'),
        ('Мультфильм', 'Мультфильм'),
        ('Комедия', 'Комедия'),
        ('Документальный фильм', 'Документальный фильм'),
        ('Ужасы ', 'Ужасы'),
        ('Научная фантастика', 'Научная фантастика'),
        ('Криминальная драма', 'Криминальная драма'),
    )

    film_title = models.CharField('Название',max_length=50, unique=True)  # название фильма
    filf_genre = models.CharField('Жанр', choices=GENRE_CHOICES, max_length=50, default='Боевик')  # жарн фильма todo: Сделать выпадающим списком
    film_description = models.TextField('Описание',max_length=1000, default='Хороший фильм') # описание к фильму
    film_photo = models.ImageField('Фото', upload_to='movies/')
    duration = models.PositiveSmallIntegerField('Длительность мин', default='45')
    start_show = models.DateField('Начало проката') # начало проката (обычная дата без времени)
    end_show =  models.DateField('Конец проката') # конец проката (обычная дата без времени)
    in_cinemas = models.BooleanField('В прокате сейчас', default=False)


    def __str__(self):
        return self.film_title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url


# class Halls(models.Model):
#     name = models.CharField('Название', max_length=30, unique=True)
#
#     def __str__(self):
#         return str(f"ID зала: {self.id}")
#
#     class Meta:
#         verbose_name = 'Зал'
#         verbose_name_plural = 'Залы'


# class Rows(models.Model):
#     room = models.ForeignKey('Halls', verbose_name="ID зала", on_delete=models.PROTECT)
#     number_row = models.PositiveSmallIntegerField('Номер ряда', validators=[MinValueValidator(1)])
#
#     def __str__(self):
#         return str(f"ID ряда: {self.id}, номер ряда: {self.number_row}")
#
#     class Meta:
#         verbose_name = 'Ряд'
#         verbose_name_plural = 'Ряды'
#         unique_together = ('room', 'number_row')



class Seats(models.Model):
    number_seat = models.PositiveSmallIntegerField('Номер места', validators=[MinValueValidator(1)])
    number_row = models.PositiveSmallIntegerField('Номер ряда', validators=[MinValueValidator(1)])


    def __str__(self):
        return str(f"Номер ряда: {self.number_row}, номер места: {self.number_seat}  ")

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        unique_together = ('number_seat', 'number_row')
        ordering = ['number_row',]



class Tickets(models.Model):
    session = models.ForeignKey('Sessions', on_delete=models.PROTECT, verbose_name='Сеанс')
    phone_number = models.BigIntegerField(verbose_name="Номер телефона", validators=[MinValueValidator(70000000000), MaxValueValidator(79999999999)])
    seat = models.ForeignKey('Seats', verbose_name='Место', on_delete=models.PROTECT)

    def __str__(self):
        return str(f'id: {self.id}')
        #str(f'ID: {self.id}, место: {self.seat} , ряд: {self.row}')

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        unique_together = ('seat', 'session' )


    def clean(self):
        validate_unique(self.seat_id,self.session_id)



