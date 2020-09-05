from django.db import models
from django.contrib.auth.models import User
from doctor.models import DoctorInfo,Schedule
from django.core.exceptions import ValidationError
import datetime

def validate_hour(value):
    hours = [str(i) for i in range(24)]
    count = 0
    for i in hours:
        if value == i:
            count+=1
    if count == 0:
        raise ValidationError(
            ('%(value)s is not hour'),
            params= {'value':value},
        )


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorInfo, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.CharField(validators=[validate_hour], max_length=2)

    def day(self):
        return self.appointment_date.strftime('%A')
    
    def clean(self):

        if not (self.day()) == (self.schedule.day):
            raise ValidationError('No Appoinment on that day!!')

        if self.appointment_date < datetime.date.today():
            raise ValidationError('Enter Valid Date!!')    

        if not (int(self.schedule.start_time)) <= (int(self.appointment_time)):
            raise ValidationError('Appointment time must for after the schedule!!')

        if (int(self.appointment_time)) > (int(self.schedule.end_time)):
            raise ValidationError('Schedule for the day is over!!')

        latest_appointment = self.doctor.appointment_set.filter(appointment_time=self.appointment_time,appointment_date=self.appointment_date).last()

        if latest_appointment:
            raise ValidationError('Appointment time already taken!!')














    
        



    
  
