import pytz
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .forms import *


from datetime import timezone
from datetime import datetime
from django.utils import timezone
from pytz import timezone as pytz_timezone

from django.shortcuts import get_list_or_404, get_object_or_404
from django.db import IntegrityError, transaction
from django.views.generic import DetailView


def film_home(request):

    end_time_str = datetime.now()
    end_time = timezone.make_aware(end_time_str, timezone.get_current_timezone())

    films = Movies.objects.filter(end_show__lt=end_time)
    for fil in films:
        fil.in_cinemas = False     # ищем все id билетов, где встречается просроченый сеанс
        fil.save()


    print(films)

    films = Movies.objects.order_by('start_show').exclude(in_cinemas=False)  # сорт по жанрам, или сделать по дате нач. проката  [:1] - выбрать одну запись
    #films.exclude(in_cinemas=False)


    print(end_time_str, end_time, datetime.now() )
    seances = Sessions.objects.filter(end_time__lt=end_time)  # Получаем все сеансы, которые уже завершились lt or gt
    print(seances)


    for seance in seances:
        tickets = Tickets.objects.filter(session=seance)  # ищем все id билетов, где встречается просроченый сеанс
        print(tickets)
        for tick in tickets:
            a = tick.seat_id  # айди каждого места ( по одному)
            seat = Seats.objects.get(pk=a)
            print(seat)
            seat.is_available = False  ## зянято ??? (нет)
            seat.save()

    tickets = Tickets.objects.all()


    return render(request, 'films/films_home.html', {'films':films, 'tickets':tickets})


 #todo: Сделать проверку вводимых данных и выдавать ошибку если что то неверно (ТЕЛЕФОН или если МЕСТА ЗАНЯТЫ УЖЕ)
def room(request):
    return render(request, 'films/films_choise.html')


def session_seats(request, session_id):  # todo: ДОДЕЛАТЬ ФОРМУ не связ. с моделью и СОХРАНЯТЬ ЛДАННЫЕ В БД  ГУГЛ
    session = get_object_or_404(Sessions, pk=session_id)
    seats = Seats.objects.filter(session=session)


    if request.method == 'POST':  # обработчик формы чтобы не сбрасывались значения при обновлении
        form = ChoiseSeat(request.POST)  #
        if form.is_valid():
            t = Tickets()
            t.session_id = request.POST.get("sessionnn")
            t.seat_id = request.POST.get("seattt")
            t.phone_number = request.POST.get("phone_number")
            t.save()
            return redirect('session_seats')
            # form.save()
    else:
        form = ChoiseSeat()

    #context = {'form': form, 'session': session, 'seats': seats,}   #'seattt': seattt, 'sessionnn': sessionnn, 'phone_number': phone_number}

    return render(request, 'films/session_seats.html', {'form': form, 'session': session, 'seats': seats,} ) #{'session': session, 'seats': seats, 'form':form})



def film_details(request, pk):
    context = {'session': Sessions.objects.filter(film_id=pk), 'film': Movies.objects.get(pk=pk)}
    return render(request, 'films/movies_detail.html', context)


def session_details(request, pk):
    error_context = ''

    if request.method == 'POST':  # обработчик формы чтобы не сбрасывались значения при обновлении
        form = ChoiseSeat(request.POST)  #
        if form.is_valid():
            session = Sessions.objects.get(pk=pk) #
            t = Tickets()
            print(session.id)
            SEATID = request.POST.get("seattt")
            SESSID = pk
            PHONEN = request.POST.get("phone_number")

            if Tickets.objects.filter(seat_id=SEATID, session_id=SESSID).exists():
                error_context = "Ошибка добавления, записть уже существует"
                return render(request, 'films/sessions_detail.html', {'error_context':error_context, 'session': Sessions.objects.get(pk=pk), 'form':form })
                #return redirect('session_seats')  #("Данная запись с таким же местом уже существует")


            t.session_id = pk
            t.seat_id = request.POST.get("seattt")
            t.phone_number = request.POST.get("phone_number")
            t.save()

            return redirect('film_home')
            # form.save()
    else:
        form = ChoiseSeat()
       # return redirect('session_details')

    context = { 'session': Sessions.objects.get(pk=pk), 'form':form, 'error_context':error_context}  #'film':  Movies.objects.filter() }



    return render(request, 'films/sessions_detail.html', context )
