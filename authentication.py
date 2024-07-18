# SPOTIFY AUTHENTICATION:

# Your Spotify username, available in your account settings on the Spotify browser client.
USERNAME = "USERNAME"

# These credentials are provided after enabling development API connections to your Spotify account.
CLIENT_ID = "CLIENT_ID"  # Client ID for Spotify API.
CLIENT_SECRET = "CLIENT_SECRET"  # Client Secret for Spotify API.

# The redirect URI, set this in your Spotify app project on the Spotify developer site.
REDIRECT_URI = "http://localhost:8888/callback"

# Optional: Device ID for Spotify, used to control playback on a specific device.
# You can get this by uncommenting and running get_device_id().
DEVICE_ID = "DEVICE_ID"

# Email address that receives your Venmo notifications.
EMAIL = "EMAIL@EMAIL.COM"


# GMAIL AUTHENTICATION:

# Uncomment and run get_label_ids() to populate these:
REQUESTS_LABEL = "LABEL1"  # Label for payment requests.
COMPLETED_LABEL = "LABEL2"  # Label for completed payments.
