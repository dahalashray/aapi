"""aapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#router
from rest_framework import routers
from doctor.views import DoctorViewset,ScheduleViewset,DoctorListView

router = routers.DefaultRouter()

router.register('doctors', DoctorViewset)
router.register('schedules', ScheduleViewset)

#swagger
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Appointment Api')

#EndPoints
urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger-docs/', schema_view),
    path('accounts/', include('accounts.urls')),
    path('', include(router.urls)),
    path('appointments/', include('Appointment.urls')),
    path('doctorlist/', DoctorListView.as_view(), name='DoctorList'),
]
