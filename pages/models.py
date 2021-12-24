from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Parish(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    Description = models.TextField()
    parish_priest = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MassType(models.Model):
    
    PERIOD_OF_THE_DAY = (
        ('MORN', 'Morning'),
        ('AFTN', 'Afternoon'),
        ('EVE', 'Evening'),
        ('MID', 'Midnight'),
        ('VIG', 'Vigil')
    )

    period = models.CharField(max_length=4, choices=PERIOD_OF_THE_DAY)

    def __str__(self):
        return self.period

class MassDay(models.Model):
    
    DAYS_OF_WEEK = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    )

    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)

    def __str__(self):
        return self.day

class Mass(models.Model):
    parish_name = models.ForeignKey(Parish, related_name='parish_masses', on_delete=models.CASCADE)
    mass_day = models.ForeignKey(MassDay, related_name='parish_mass_days', on_delete=models.CASCADE)
    mass_period = models.ForeignKey(MassType, related_name='parish_mass_types', on_delete=models.CASCADE)
    start_time = models.TimeField()

    def __str__(self):
        return f'{self.parish_name} {self.mass_day} {self.start_time}'