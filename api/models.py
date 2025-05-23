from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):
    rider = models.ForeignKey(User, on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    ride_status = models.CharField(max_length=20, choices=[
        ('REQUESTED', 'Requested'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed')
    ], default='REQUESTED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
