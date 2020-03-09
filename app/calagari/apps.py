from django.apps import AppConfig


class CalagariConfig(AppConfig):
    name = 'calagari'
    verbose_name = 'Calagari'
    # Anyone can create venues, events and tags
    # Allowed values: 
    CREATION_SETTINGS = ["FREE_CREATION", "FREE_SUBMISSION", "BLOCK_SUBMISSION"]
    # FREE_CREATION - Anyone can create an event
    # FREE_SUBMISSION - Anyone can SUBMIT an event, which has then to be approved
    # BLOCK_SUBMISSION - Only who has permission can create events
    # These values are contained inside "CREATION_SETTINGS"
    event_creation = "FREE_CREATION"
    # Same as EVENT_CREATION, but for venues
    venue_creation = "FREE_CREATION"
    # Same as EVENT_CREATION, but for tags
    tag_creation = "FREE_CREATION"

    # Require an user accoutn for EVENT_CREATION, VENUE_CREATION and TAG_CREATION
    require_registration_creation = False
    # Require registration for even seeing events and venues
    require_registration_venue = False

    # API Key for Google Maps services
    google_maps_api_key = "<something something>"
        
