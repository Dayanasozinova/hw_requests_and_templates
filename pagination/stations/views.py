import csv

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination import settings

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    data = []
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(data, 10)
    page = paginator.get_page(page_number)

    try:
        bus_stations = paginator.page(page_number)
    except PageNotAnInteger:
        bus_stations = paginator.page(1)
    except EmptyPage:
        bus_stations = paginator.page(paginator.num_pages)

    context = {
        'bus_stations': bus_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

