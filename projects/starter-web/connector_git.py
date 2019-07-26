from vivialconnect import Resource, Message

# Configure SDK
Resource.api_key = ""
Resource.api_secret = ""
Resource.api_account_id = ""


# Send a single message from a Connector
def send_sms_connector(to_number=None, connector_id=None, body=None):
    message = Message()
    message.to_number = to_number
    message.body = body
    message.connector_id = connector_id
    message.send()

    # Print message ID and Status
    output = "Message {} {} {}".format(message.id, message.status, message.body)
    print(output)

#Send a batch of messages
def send_batch(num=5):
    msg_template = "Message #{} sent from a Connector"

    for x in range(1, (num+1)):
        send_sms_connector(to_number="",
                     connector_id = 000,
                     body=msg_template.format(x))
