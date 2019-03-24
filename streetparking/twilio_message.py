from __future__ import unicode_literals

from twilio.rest import Client
from django.core.exceptions import MiddlewareNotUsed
import os
import logging
import json


"""
sends text message to the person with details about the ticket in the body
"""

logger = logging.getLogger(__name__)

body = "This is a test message from twilio https://www.google.com/"

def load_twilio_config():
    twilio_account_sid = "AC5abd8890d711f60ea1359148778f0a20"
    twilio_auth_token = "7956c6510ab7d2ed2098ac3a4f96caa4"
    twilio_number = "+17326466332"

    return (twilio_number, twilio_account_sid, twilio_auth_token)


class MessageClient(object):
    def __init__(self):
        (twilio_number, twilio_account_sid,
         twilio_auth_token) = load_twilio_config()

        self.twilio_number = twilio_number
        self.twilio_client = Client(twilio_account_sid,
                                              twilio_auth_token)

    def send_message(self, body1, to):
        self.twilio_client.messages.create(body=body1, to=to,
                                           from_=self.twilio_number,
                                           # media_url=['https://demo.twilio.com/owl.png'])
                                           )


mc = MessageClient()
mc.send_message(body,7327151517)