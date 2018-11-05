Debug app to show different billing_reason on invoice events with Stripe API version 2018-10-31

Relates to https://github.com/dj-stripe/dj-stripe/issues/758

Installation:

* (recommended) create a new python virtualenv (tested with python 2.7 and 3.6)
* pip install -r requirements.txt

Example:

1) Start app with:

```bash
STRIPE_API_KEY=sk_test_YOURSECRETKEY python app.py
```

2) Create a webhook on stripe dashboard pointing at local 127.0.0.1:5000/stripe/webhook/ (eg via an ngrok tunnel) 
3) Create a subscription via the stripe dashboard
4) Observe logging in console - billing_reason is different for a given event id when recieved as a webhook vs retrieving the same event from the API.
