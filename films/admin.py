from django.contrib import admin
from films.models import * #Movies, Sessions, Halls, Tickets, Seats
# Register your models here.

# убрать ЕСЛИ ЧО
@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'film_title' ,'duration', 'start_show', 'end_show', 'in_cinemas')
    #list_display_links = ('film_title')
    #search_fields = ('film_title', 'end_show')  ---- сортировка по полям
    list_editable = ('in_cinemas', 'start_show', 'end_show' , 'duration') # редактируемое поле
    pass

@admin.register(Sessions)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id','film' , 'start_time', 'end_time', 'price')
    #search_fields = ('film', 'room')
    list_editable = ( 'start_time', 'price') ####Fsdfdsfsdfd

    pass


@admin.register(Seats)
class SeatsAdmin(admin.ModelAdmin):
    list_display = ('id','number_seat','number_row')
    pass

@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id','session', 'seat', 'phone_number')
    #search_fields = ('session', 'seat')
    pass


# @admin.register(Halls)
# class HallsAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     pass

# @admin.register(Rows)
# class RowsAdmin(admin.ModelAdmin):
#     list_display = ('id','room','number_row')
#     pass
#

# @admin.register(CinemaSeat)
# class CinemaSeatAdmin(admin.ModelAdmin):
#     list_display = ('row','seat_number','is_reserved')
#     pass