from vivialconnect import Resource, Message, Attachment

# Configure SDK
Resource.api_key = "MTKOVFNVYKUOPQFD9LZTLYQZRJAGW4VUJLV"
Resource.api_secret = "kuvwFXgKXson8JYomc5OPurrEoa96cWfTlOg7PXob8mvEeRh"
Resource.api_account_id = "10193"

# Set up Message object
from_number = "+16124282883"
to_number = "+13202930706"

message = Message()
message.media_urls = ['http://prod.static.vikings.clubs.nfl.com/nfl-assets/img/gbl-ico-team/MIN/logos/home/large.png']
message.from_number = from_number
message.to_number = to_number