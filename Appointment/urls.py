from django.urls import path
from .views import AppointmentCreateView,AppointmentListView,AppointmentCreateView,AppointmentDeleteView

urlpatterns = [
    path('list/', AppointmentListView.as_view(), name = 'AppointmentList'),
    path('create/', AppointmentCreateView.as_view(), name = 'AppointmentCreate'),
    path('delete/<int:pk>/', AppointmentDeleteView.as_view(), name = 'AppointmentDelete'),
]

