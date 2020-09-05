from .models import DoctorInfo,Schedule
from .serializers import DoctorSerializer,ScheduleSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated


class DoctorViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = DoctorInfo.objects.all()
    serializer_class = DoctorSerializer


class ScheduleViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer