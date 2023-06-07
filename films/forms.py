from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.db.models import *
from django.db.models import Q



class ChoiseSeat(forms.Form):
    #variable = forms.CharField(widget=forms.HiddenInput())


    mas = []
    tickets = Tickets.objects.all()   # ищем все id билетов, где встречается просроченый сеанс


    for tick in tickets:
        #tic_seans = tick.session.id  # айди сеанса
        #t = tick.objects.filter(session_id=tick.session.id)  # все билеты для сеанса КОНКРЕТНОГО

        #seat = Seats.objects.get(tickets)


        s = tick.seat_id  # id места

        seat = Seats.objects.get(pk=s)
        mas.append(s)  # айди занятых мест, потом исключаем
        #aaa = Seats.objects.exclude(tickets__session_id=tic_seans)
#        print(f'ffffffffffff {aaa}')

    print(mas)

    aaa = Seats.objects.exclude(pk__in=mas) # получаем остальные места (незанятые)

    print(f'Осталось мест: {aaa.count()}')
   # print(variable)

    seattt = forms.ModelChoiceField(queryset=Seats.objects.all(), label="Место")  # БРАТЬ МЕСТА ПРИВЯЗАННЫЕ К КОНКРЕТНОМУ СЕАНСУ ЕЩЁ


    phone_number = forms.IntegerField(max_value=79999999999, min_value=70000000000, label="Номер телефона")

    #sessionnn = forms.ModelChoiceField(queryset=Sessions.objects.all(), label="Сеанс")



class ChoiseSession(forms.Form):
    variable = forms.IntegerField(widget=forms.HiddenInput())

    #seattt = forms.ModelChoiceField(queryset=aaa, label="Место")  # БРАТЬ МЕСТА ПРИВЯЗАННЫЕ К КОНКРЕТНОМУ СЕАНСУ ЕЩЁ

    #query = Sessions.objects.all().filter(film_id=1)
    seanses = forms.ModelChoiceField(queryset=Sessions.objects.all(), label="Сеанс")
    print(seanses)


class ChoiseFilm(forms.ModelForm):

    #seat = forms.ModelChoiceField(queryset=Tickets.objects.all())

    class Meta:
        model = Tickets
        fields = 'seat', 'phone_number'  #'__all__' #todo:связать эту форму с формой где занимаем места

        # tickets = Tickets.objects.all()  # ищем все id билетов, где встречается просроченый сеанс
        # print(tickets)
        # for tick in tickets:
        #     a = tick.seat_id  # айди каждого места ( по одному)
        #     seat = Seats.objects.get(pk=a)
        #




    # def clean(self):
    #     super(ChoiseFilm, self).clean()
    #     phone_number = self.cleaned_data['phone_number']
    #     # if len(str(self.oh phone_number)) < 11 or len(str(phone_number)) > 11:
    #     #     raise forms.ValidationError('Неверный формат номера телефона')
    #
    #     if  len(str(self.cleaned_data['phone_number'])) < 11:
    #         self._errors['phone_number'] = 'your password\'s length is too short'
    #         # you may also use the below line to custom your error message, but it doesn't work with me for some reason
    #         raise forms.ValidationError('Your password is too short')
    #
    #     return phone_number


    # def validate_phone_number(phone_number):  #НЕ РАБ. ВЫШЕ
    #     if len(str(phone_number)) < 11 or len(str(phone_number)) > 11:
    #         raise ValidationError('Неверный формат номера телефона')



