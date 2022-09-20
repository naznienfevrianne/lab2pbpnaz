from django.shortcuts import render
from mywatchlist.models import FilmItem
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def show_watchlist(request):
    data_watchlist = FilmItem.objects.all();
    context = {
        'list_film': data_watchlist,
        'name' : 'Naznien Fevrianne Malano',
        'npm' : '2106751404'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = FilmItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = FilmItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")