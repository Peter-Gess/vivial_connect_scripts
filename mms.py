# Sending a picture message using the Vivial Connect Python SDK

from vivialconnect import Resource, Message, Attachment

# Configure SDK
Resource.api_key = ""
Resource.api_secret = ""
Resource.api_account_id = ""

# Set up Message object
from_number = ""
to_number = ""

message = Message()
message.media_urls = ['http://prod.static.vikings.clubs.nfl.com/nfl-assets/img/gbl-ico-team/MIN/logos/home/large.png']
message.from_number = from_number
message.to_number = to_number
