#!/usr/bin/env python

"""
Debug app to show different billing_reason on invoice events with Stripe API version 2018-10-31

Relates to https://github.com/dj-stripe/dj-stripe/issues/758
"""

from __future__ import print_function

import os

import stripe
from flask import Flask, request

app = Flask(__name__)

stripe.api_key = os.environ.get("STRIPE_API_KEY")
stripe.api_version = "2018-10-31"


@app.route("/stripe/webhook/", methods=["POST"])
def webhook():
    webhook_data = request.json

    print(
        "api_version={} object={} id={} type={}".format(
            webhook_data["api_version"],
            webhook_data["object"],
            webhook_data["id"],
            webhook_data["type"],
        )
    )

    if webhook_data["type"].startswith("invoice."):
        webhook_billing_reason = webhook_data["data"]["object"]["billing_reason"]
        event_id = webhook_data["id"]
        api_data = stripe.Event.retrieve(event_id)

        retrieved_billing_reason = api_data["data"]["object"]["billing_reason"]

        if webhook_billing_reason == retrieved_billing_reason:
            print(
                "event {} got same billing_reason for webhook and retrieve: {}".format(
                    event_id, webhook_billing_reason
                )
            )
        else:
            print(
                "event {} got different billing_reason for webhook and retrieve: {} != {}".format(
                    event_id, webhook_billing_reason, retrieved_billing_reason
                )
            )

    return ""


if __name__ == "__main__":
    app.run()
