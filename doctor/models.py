from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_day(value):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    count = 0
    for i in days:
        if value == i:
            count+=1
    if count == 0:
        raise ValidationError(
            ('%(value)s is not day'),
            params= {'value':value},
        )

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

        
class DoctorInfo(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')
    department = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return (self.name) + (self.department)

    class meta():
        ordering = ('Department','Name',)       


class Schedule(models.Model):
    doctor = models.ForeignKey(DoctorInfo, on_delete=models.CASCADE)
    day = models.CharField(validators=[validate_day], max_length=10)
    start_time = models.CharField(validators=[validate_hour], max_length=2)
    end_time = models.CharField(validators=[validate_hour], max_length=2)

    def __str__(self):
        return (self.doctor.name) +  (self.day)



