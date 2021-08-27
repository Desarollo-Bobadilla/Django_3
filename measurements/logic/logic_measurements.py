import measurements
from ..models import Measurement

def get_all_measurements():
    return Measurement.objects.all()

def get_measurement_pk(n):
    return Measurement.objects.get(pk = n)

def delete_measurement_pk(n):
    Measurement.objects.filter(pk = n).delete()

def change_value_measurement_pk(n):
    measurements = Measurement.objects.get(pk = n)
    measurements.value = 10
    measurements.save()