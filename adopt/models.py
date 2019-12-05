from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    unique_squirrel_id = models.CharField(max_length=100)
    SHIFT_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
    )
    shift = models.CharField(
            max_length=3,
            choices=SHIFT_CHOICES,
            default='AM',
    )
    date
    age
    primary_fur_color
    location
    specific_location
    running
    chasing
    climbing
    eating
    foraging
    other_activities
    kuks
    quaas
    moans
    tail_flags
    tail_twitches
    approaches
    indifferent
    runs_from
