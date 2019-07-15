# Sending a message via the CLI using the Vivial Connect Python SDK
# Interact with this script in the Python Shell by running python -i sms.py

from vivialconnect import Resource, Message

# Configure SDK
Resource.api_key = ""
Resource.api_secret = ""
Resource.api_account_id = ""

# GET most recent message
def getm():
    return Message.find_first(order="id desc")


# Set up Message object
from_number = ""
to_number = ""


# Send Message
message = Message()
message.from_number = from_number
message.to_number = to_number
