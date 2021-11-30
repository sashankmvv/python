from django.db import models
from ngo.models import EventManager
from django.urls import reverse

# Create your models here.

class PostEvent(models.Model):
    event_id = models.AutoField
    event_organiser = models.ForeignKey(EventManager, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    event_manager = models.CharField(max_length=100)
    event_contact = models.CharField(max_length=13)
    event_address = models.CharField(max_length=200)
    event_location = models.CharField(max_length=100)
    event_city = models.CharField(max_length=100)
    event_state = models.CharField(max_length=100)
    event_zipcode = models.CharField(max_length=10)
    event_foodqty = models.PositiveIntegerField(default=0)
    event_type = models.CharField(max_length=100, default='')
    event_status = models.BooleanField(default=False)
    event_lat = models.CharField(max_length=100, default='')
    event_lon = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('event-home')