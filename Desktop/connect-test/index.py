import vivialconnect

from vivialconnect import Resource, Message
import requests

Resource.api_key = "MTK7UAKH7V6T3JVCRUB205NAPVEYRAIZB27"
Resource.api_secret = "S24wKQcLTAXALx5CuujZJGDockS6NQQMhmLjOaKvxjNeyN2Y"
Resource.api_account_id = "10193"

def send_message(to_number=None, from_number=None, body=None):
    message = Message()
    message.from_number = from_number
    message.to_number = to_number
    message.body = body
    message.send()

send_message(to_number='+13202930706',
             from_number='+13202457424',
             body='test message')
