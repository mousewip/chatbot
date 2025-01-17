# -*- coding: utf-8 -*-

import json
import requests
from flask import request

from Project import *


def send_message(recipient_id, message_text):

    print("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": app.config["FB_PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        # log(r.status_code)
        # log(r.text)
        pass


@app.route('/fb', methods=['GET'])
def fb_verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == app.config["FB_VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/fb', methods=['POST'])
def fb_webhook():
    # endpoint for processing incoming messaging events

    data = request.get_json()
    print(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]  # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]

                    print("Sender ID : " + str(sender_id))
                    print("Receipt ID : " + str(recipient_id))
                    # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text

                    print('FB req mess: ' + message_text)

                    rs = Predict(message_text, 'FB')

                    send_message(sender_id, rs)

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

                # if messaging_event.get("read"):  # user clicked/tapped "postback" button in earlier message
                #     sender_id = messaging_event["sender"]["id"]  # the facebook ID of the person sending you the message
                #     recipient_id = messaging_event["recipient"]["id"]
                #     # the recipient's ID, which should be your page's facebook ID
                #     message_text = messaging_event["message"]["text"]  # the message's text
                #
                #     send_message(sender_id, "Read không rep chú m!")
                #     pass

    return "ok", 200
