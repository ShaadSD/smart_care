from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
# Create your views here.
from . import models
class AppointmentViewsSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializers

    def get_queryset(self):
        queryset = super.get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
            
        
    
