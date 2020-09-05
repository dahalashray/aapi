from rest_framework import serializers
from .models import DoctorInfo,Schedule

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorInfo
        fields = ['name', 'photo', 'department', 'address', 'description',]

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['doctor', 'day', 'start_time', 'end_time',]