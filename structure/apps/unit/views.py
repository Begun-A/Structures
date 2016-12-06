from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from apps.unit.models import Unit, Room, Structure
from apps.unit.utils import UnitObj


def get_unit_list(request):
    units = Unit.objects.all()
    return render(request, 'units_list.html', {'units': units})


def get_unit(request, pk):
    unit = Unit.objects.get(pk=pk)
    return render(request, 'unit.html', {'unit': unit})


def get_possible_rooms(request):
    if request.method != 'POST':
        return render(request, 'error.html', {})
    data = request.POST.dict()
    unit = Unit.objects.get(pk=data['unit_id'])
    length = int(data['length'])
    width = int(data['width'])
    u = UnitObj(length, width)
    u.calculate_possible_rooms()
    return render(request, 'possible-rooms.html',
                  {'unit': unit, 'possible_rooms': u.possible_rooms,
                   'length': length, 'width': width})


def create_structure(request):
    if request.method != 'POST':
        return render(request, 'error.html', {})
    data = request.POST.dict()
    structure = Structure.objects.create(name=data['name'],
                                         length=int(data['length']),
                                         width=int(data['width']),
                                         unit=Unit.objects.get(
                                             pk=int(data['id'])))
    Room.objects.create(length=int(data['length1']), width=data['width1'],
                        structure=structure)
    Room.objects.create(length=int(data['length2']), width=data['width2'],
                        structure=structure)
    Room.objects.create(length=int(data['length3']), width=data['width3'],
                        structure=structure)
    return HttpResponseRedirect(reverse('structures-list'))


def structure_list(request):
    structures = Structure.objects.all()
    return render(request, 'structures.html', {"structures": structures})


def get_structure(request, pk):
    return render(request, 'error.html', {})


def update_structure(request, pk):
    return render(request, '', {})


def delete_sturcture(request, pk):
    return HttpResponseRedirect()
