from measurements.logic.logic_measurements import get_all_measurements
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurement_list'),
    path('see/<int:pk>/', views.get_measurement, name='get_measurement_by_pk'),
    path('delete/<int:pk>/', views.delete_measurement, name='delete_measurement_by_pk'),
    path('change/<int:pk>/', views.change_measurement, name='change_measurement_by_pk')
]