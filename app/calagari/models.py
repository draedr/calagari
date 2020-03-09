from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    # Indicates if its a draft. Will not be listed.
    # An event which uses Day objects shall first be created as draft
    # then added the days, and at the end, published
    is_draft = models.BooleanField(default=True)
    # The description of the event. Must have corresponding mediatype in description_mediatype
    description_content = models.TextField(blank=True, null=True)
    description_mediatype = models.CharField(max_length=127, default="plain/text")
    # Indicates the venue (the location) of the event.
    # It can reference to:
    # - A previously created venue
    # - A purpose created venue (created from the same form)
    # - Nothing (for example, for city-wide events)
    location = models.ForeignKey('Venue', models.SET_NULL, null=True, blank=True)

    # Generic contact info that are not an url, an email or a phone number
    contact_info = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    mail = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)

    # Indicates if the event requires booking
    booking_enabled = models.BooleanField(default=True)
    # Indicates if booking info are saved inside the day.
    # If (True) then, (booking_info, spots, start_booking, end_booking)
    # in Event will be unused, instead will be used the one in the Day object
    booking_per_day = models.BooleanField(default=False)
    # Indicates if booking is allowed only in the spcified timeframe
    booking_time_slot = models.BooleanField(default=False)
    # Indicates if the bookings will be automatically accepted or need 
    # the owner to accept it
    booking_automatic_accepted = models.BooleanField(default=False)

    # Info about the booking, like required info, etc.
    booking_info = models.TextField(blank=True, null=True)
    # Maximum spots available for the booking
    spots = models.IntegerField(null=True)
    # Start of booking time slot
    start_booking = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    # End of booking time slot
    end_booking = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    tags = models.ManyToManyField("Tag")

class Day(models.Model):
    event = models.ForeignKey("Event", models.CASCADE)
    start = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    info = models.TextField(blank=True, null=True)
    
    # These fields are equal to the one inside Event
    # Info about the booking, like required info, etc.
    booking_info = models.TextField(blank=True, null=True)
    # Maximum spots available for the booking
    spots = models.IntegerField(null=True)
    # Start of booking time slot
    start_booking = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    # End of booking time slot
    end_booking = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

class Booking(models.Model):
    event = models.ForeignKey("Event", models.CASCADE, null=False)
    day = models.ForeignKey("Day", models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, models.CASCADE, null=False)
    additional_info = models.TextField(blank=True, null=True)
    # Indicates the status of the booking acceptance
    # It can have these values:
    # - None/Null = Pending 
    # - True = Accepted
    # - False = Refused
    status = models.BooleanField(blank=False, default=None, null=True)

    class Meta:
        unique_together = ['event', 'day', 'user']

class Tag(models.Model):
    slug = models.CharField(max_length=30)
    name = models.CharField(max_length=60)

class Venue(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    # The description of the event. Must have corresponding mediatype in description_mediatype
    description_content = models.TextField(blank=True, null=True)
    description_mediatype = models.CharField(max_length=127, default="plain/text")
        
    # Generic contact info that are not an url, an email or a phone number
    contact_info = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    mail = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)

    address = models.CharField(max_length=230, blank=True, null=True)
    lat = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=8)
    lon = models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=8)
    global_plus_code = models.CharField(max_length=230, blank=True, null=True)

    tags = models.ManyToManyField("Tag")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=False, blank=False)
    info = models.TextField(null=True, blank=True)

    # These are needed when a creation setting is set to "BLOCK_SUBMISSION"
    allow_create_events = models.BooleanField(default=True)
    allow_create_venues = models.BooleanField(default=False)
    allow_create_tags = models.BooleanField(default=False)