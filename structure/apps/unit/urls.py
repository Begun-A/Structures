from django.conf.urls import url, patterns
from apps.unit.views import get_unit_list, structure_list, get_unit, get_possible_rooms, get_structure, create_structure

urlpatterns = [
    url(r'^$', get_unit_list, name='units-list' ),
    url(r'^structures/$', structure_list, name='structures-list'),
    url(r'^units/(?P<pk>\d+)/', get_unit, name='unit'),
    url(r'^possible-rooms/$',get_possible_rooms, name='possible-rooms' ),
    url(r'^structures/(?P<pk>\d+)/', get_structure, name='structure'),
    url(r'^structure/create/$', create_structure, name='create-structure')

]