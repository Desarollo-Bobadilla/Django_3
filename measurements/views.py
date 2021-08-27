
from .logic.logic_measurements import *
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements_list = serializers.serialize('json', get_all_measurements())
    return HttpResponse(measurements_list, content_type = 'application/json')

def get_measurement(request, pk):
    measurements = serializers.serialize('json', [get_measurement_pk(pk)])
    return HttpResponse(measurements, content_type = 'application/json')

def delete_measurement(request, pk):
    delete_measurement_pk(pk)

    measurements_list = serializers.serialize('json', get_all_measurements())
    return HttpResponse(measurements_list, content_type = 'application/json')

def change_measurement(request, pk):
    change_value_measurement_pk(pk)

    measurements_list = serializers.serialize('json', get_all_measurements())
    return HttpResponse(measurements_list, content_type = 'application/json')