from .models import DoctorInfo,Schedule
from .serializers import DoctorSerializer,ScheduleSerializer
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated


class DoctorViewset(viewsets.ModelViewSet):                         #For Admin Purpose(OPTIONAL)
    permission_classes = [IsAdminUser]
    queryset = DoctorInfo.objects.all()
    serializer_class = DoctorSerializer


class ScheduleViewset(viewsets.ModelViewSet):                       #For Admin Purpose(OPTIONAL)
    permission_classes = [IsAdminUser]
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class DoctorListView(generics.ListAPIView):                         
    permission_classes = [IsAuthenticated]                           #Browsing Doctors
    queryset = DoctorInfo.objects.all()
    serializer_class = DoctorSerializer


