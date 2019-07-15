# Simple Flask App daemon process to receive callback_listener requests
# Recommended that you use ngrok to expose a local port to the web to receive data from callback

import datetime
import json

import requests
from flask import Flask, request, Response
from vivialconnect import Resource, Number, Message
import socket


app = Flask(__name__)


@app.route("/incoming_messages_status", methods=["POST"])
def message_status_callback():

    if request.json:

        content = request.get_json()

        print(
            "[STATUS] Message ID: {}\tMessage Status: {}\tTimestamp: {}".format(
                content["message_id"], content["status"], content["timestamp"]
            )
        )

    return Response()


@app.route("/incoming_messages", methods=["POST"])
def incoming_message_callback():

    if request.json:

        content = request.get_json()

        print(
            "[INCOMING MSG] From: {}\tTo: {}\tType: {}\tMsg ID: {}\tStatus: {}\tTime: {}".format(
                content["from_number"],
                content["to_number"],
                content["message_type"],
                content["message_id"],
                content["status"],
                content["sent"],
            )
        )

    return Response()


if __name__ == "__main__":
    app.run(debug=True)
