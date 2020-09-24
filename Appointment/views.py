from django.shortcuts import render
from rest_framework import generics,status
from .models import Appointment
from .serializers import AppointmentSerializer,AppointmentPostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated,]
    queryset = Appointment.objects.all()

    def list(self, request, *args, **kwargs):                              #Overriding list() for permissions
        if request.user.is_superuser:
            queryset = self.filter_queryset(self.get_queryset())           #Admin can only access all the appointments(OPTIONAL)
        
        else:
            queryset = self.queryset.filter(patient=request.user)          #User can only access their own appointments

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AppointmentCreateView(generics.CreateAPIView):                        #Creating Appointment
    serializer_class = AppointmentPostSerializer
    model = Appointment
    permission_classes = [IsAuthenticated,]


class AppointmentDeleteView(generics.DestroyAPIView):                       #Deleting Appointment
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated,]
    queryset = Appointment.objects.all()

    def destroy(self, request, *args, **kwargs):                             #Overriding destroy() so that user can only delete their own appointments
        instance = self.get_object()
        if request.user == instance.patient:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)














    
