from django.shortcuts import render
from django.http import HttpResponse

from datetime import timezone
from datetime import datetime
import datetime
from django.utils import timezone
from .models import *
from films.forms import *
# Create your views here.

def index(request):
    end_time_str = datetime.datetime.now()
    end_time = timezone.make_aware(end_time_str, timezone.get_current_timezone())

    films = Movies.objects.filter(end_show__gte=end_time)

    return render(request, 'main/index.html', {'films':films} )

# def about(request):
#     return render(request, 'main/about.html')


