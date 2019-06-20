from vivialconnect import Resource, Message

# Configure SDK
Resource.api_key = "MTKOVFNVYKUOPQFD9LZTLYQZRJAGW4VUJLV"
Resource.api_secret = "kuvwFXgKXson8JYomc5OPurrEoa96cWfTlOg7PXob8mvEeRh"
Resource.api_account_id = "10193"

# GET most recent message
def getm():
    return Message.find_first(order="id desc")


# Set up Message object
from_number = "+16122042587"
to_number = "+13202930706"

message = Message()
message.from_number = from_number
message.to_number = to_number