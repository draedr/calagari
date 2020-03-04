# Anyone can create venues, events and tags
# Allowed values: 
# 
# FREE_CREATION - Anyone can create an event
# FREE_SUBMISSION - Anyone can SUBMIT an event, which has then to be approved
# BLOCK_SUBMISSION - Only who has permission can create events
EVENT_CREATION = "FREE_CREATION"
# Same as EVENT_CREATION, but for venues
VENUE_CREATION = "FREE_CREATION"
# Same as EVENT_CREATION, but for tags
TAG_CREATION = "FREE_CREATION"

# Require an user accoutn for EVENT_CREATION, VENUE_CREATION and TAG_CREATION
REQUIRE_REGISTRATION_CREATION = False

# Require registration for even seeing events and venues
REQUIRE_REGISTRATION_VIEWING = False

# The name of the folder which contains the theme. Default to blank, which means no sub-directory
THEME_NAME = ""

# API Key for Google Maps services
GOOGLE_MAPS_API_KEY = "<something something>"