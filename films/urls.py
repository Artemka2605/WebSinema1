from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.film_home, name='film_home'),
    #path('choise', views.film_choise, name='film_choise'),
    #path('thanks/', views.thanks_page, name='thanks_page'),
    path('room', views.room, name='room'),  #cinema_seats

    path('sessions/<int:pk>', views.session_details, name='session_seats'),
    path('<int:pk>', views.film_details, name='film_details'),  # films/1 и тд.

    #path('<int:pk>', views.FilmsDetailView.as_view(), name='film_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)