from django.shortcuts import render
from django.http import HttpResponseRedirect

from apps.unit.models import Unit


def get_unit_list(request):
    units = Unit.objects.all()
    return render(request, '', {'units': units})

def get_unit(request, pk):
    return render(request, '', {})

def get_possible_rooms(request):
    return render(request, '', {})

def create_structure(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass

def structure_list(request):
    return render(request, '', {})

def get_structure(request, pk):
    return render(request, '', {})

def update_structure(request, pk):
    return render(request, '', {})

def delete_sturcture(request, pk):
    return HttpResponseRedirect()


