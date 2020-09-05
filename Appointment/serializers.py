from rest_framework import serializers
from .models import Appointment
from doctor.serializers import DoctorSerializer
from doctor.serializers import ScheduleSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    schedule = ScheduleSerializer()
    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'doctor', 'schedule', 'appointment_date', 'appointment_time',)
        read_only_fields = ('id',)


class AppointmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'schedule', 'doctor', 'appointment_date', 'appointment_time',)
        read_only_fields = ('id',)




