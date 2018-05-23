from striped import app
from flask import render_template, request, redirect
import json
import stripe

SIGNS = {
    'usd': '$',
    'eur': '€'
}

@app.route('/')
def index():
    return redirect("https://qgis.org/en/site/getinvolved/donations.html", code=302)


@app.route('/test')
def test():
    # make sure you have the properties STRIPE_PUBLISHABLE_KEY and STRIPE_FORM_URL in your config !
    return render_template('index.html',
                           key=app.config['STRIPE_PUBLISHABLE_KEY'],
                           stripeformurl=app.config['STRIPE_FORM_URL'])

@app.route('/form')
def form():
    # make sure you have the properties STRIPE_PUBLISHABLE_KEY and STRIPE_CHARGE_URL in your config !
    return render_template('stripeform.html',
                           key=app.config['STRIPE_PUBLISHABLE_KEY'],
                           stripechargeurl=app.config['STRIPE_CHARGE_URL'])

@app.route('/chargejson', methods=['POST'])
def chargejson():
    token = request.form['stripeToken']
    donorname = request.form['donorname']
    email = request.form['email']
    raw_amount = request.form['amount'].split(':')
    currency = raw_amount[0]
    amount = raw_amount[1]
    customer = stripe.Customer.create(
        source=token
    )
    # charge object: https://stripe.com/docs/api/python#charges
    # charge.amount  # ALWAYS in cents!
    # charge.currency
    # charge.description (the one you sent below in the dict)
    # charge.outcome   object with payment acceptance details
    # charge.paid
    # charge.status ('succeeded')
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency=currency,
        description='QGIS Donation',
        metadata={'email': email, 'donorname': donorname}
    )

    result = {'result': 'error', 'data': charge}
    if charge.paid:
        result = {'result': 'ok', 'donation': '{} ({}) {}{:0,.2f} !'.format(donorname, email, SIGNS[currency], int(amount)/100)}

    return json.dumps(result)

    #return json.dumps(charge)
    # {
    #     "id": "zzzzzz",
    #     "object": "charge",
    #     "amount": 1000,
    #     "amount_refunded": 0,
    #     "application" : null,
    #     "application_fee": null,
    #     "balance_transaction": "zzzzzz",
    #     "captured": true,
    #     "created": 1526911084,
    #     "currency": "eur",
    #     "customer": "zzzzz",
    #     "description": "QGIS Donation",
    #     "destination": null,
    #     "dispute": null,
    #     "failure_code": null,
    #     "failure_message": null,
    #     "fraud_details" : {},
    #     "invoice": null,
    #     "livemode": false,
    #     "metadata": {},
    #     "on_behalf_of": null,
    #     "order": null,
    #     "outcome" :
    #         {"network_status": "approved_by_network",
    #          "reason": null,
    #          "risk_level": "normal",
    #          "seller_message" : "Payment complete.",
    #          "type": "authorized"
    #          },
    #     "paid": true,
    #     "receipt_email": null,
    #     "receipt_number": null,
    #     "refunded": false,
    #     "refunds": {
    #         "object": "list",
    #         "data": [],
    #         "has_more": false,
    #         "total_count" : 0,
    #         "url": "/v1/charges/zzzzzz"
    #         },
    #     "review": null,
    #     "shipping": null,
    #     "source" : {
    #         "id": "card_zzzzzz",
    #         "object": "card",
    #         "address_city": null,
    #         "address_country": null,
    #         "address_line1": null,
    #         "address_line1_check": null,
    #         "address_line2": null,
    #         "address_state": null,
    #         "address_zip": null,
    #         "address_zip_check": null,
    #         "brand": "Visa",
    #         "country": "US",
    #         "customer": "cus_zzzzz",
    #         "cvc_check": "pass",
    #         "dynamic_last4": null,
    #         "exp_month": 1,
    #         "exp_year": 2020,
    #         "fingerprint": "zzzzz",
    #         "funding": "credit",
    #         "last4": "4242",
    #         "metadata": {},
    #         "name": null,
    #         "tokenization_method": null
    #         },
    #     "source_transfer": null,
    #     "statement_descriptor": null,
    #     "status": "succeeded",
    #     "transfer_group": null
    # }


#
# @app.route('/elements', methods=['GET'])
# def elements():
#     amount = 1000  # cents!!
#     currency = 'usd'
#     currency_sign = SIGNS[currency]
#     return render_template('elements0.html', key=app.config['STRIPE_PUBLISHABLE_KEY'])
#
# @app.route('/charge2', methods=['POST'])
# def charge2():
#     token = request.form['stripeToken']
#     donorname = request.form['donorname']
#     email = request.form['email']
#     raw_amount = request.form['amount'].split(':')
#     currency = raw_amount[0]
#     amount = raw_amount[1]
#     customer = stripe.Customer.create(
#         source=token
#     )
#     # charge object: https://stripe.com/docs/api/python#charges
#     # charge.amount  # ALWAYS in cents!
#     # charge.currency
#     # charge.description (the one you sent below in the dict)
#     # charge.outcome   object with payment acceptance details
#     # charge.paid
#     # charge.status ('succeeded')
#     charge_obj = stripe.Charge.create(
#         customer=customer.id,
#         amount=amount,
#         currency=currency,
#         description='QGIS Donation'
#     )
#
#     # TODO checking of returned charge object
#
#     amount = charge_obj.amount
#     currency = SIGNS[charge_obj.currency]
#
#     return render_template('charge.html', amount=amount, currency=currency, email=email, donorname=donorname)
#
# @app.route('/charge', methods=['POST'])
# def charge():
#     currency = request.form['currency']
#     amount = request.form['amount']
#     email = request.form['stripeEmail']
#     token = request.form['stripeToken']
#
#     customer = stripe.Customer.create(
#         source=token
#     )
#     # charge object: https://stripe.com/docs/api/python#charges
#     # charge.amount  # ALWAYS in cents!
#     # charge.currency
#     # charge.description (the one you sent below in the dict)
#     # charge.outcome   object with payment acceptance details
#     # charge.paid
#     # charge.status ('succeeded')
#     charge_obj = stripe.Charge.create(
#         customer=customer.id,
#         amount=amount,
#         currency=currency,
#         description='QGIS Donation'
#     )
#
#     # TODO checking of returned charge object
#     return render_template('charge.html', amount=amount, currency=currency, email=email)
#

# @app.route('/charge', methods=['POST'])
# def charge():
#     # Amount in cents
#     amount = 500
#     #amount = request.form['amount']
#     currency = 'eur'
#     email = request.form['stripeEmail']
#
#     customer = stripe.Customer.create(
#         #email='customer@example.com', # ?? for testing you need customer@example.com?
#         #email=request.form['stripeEmail'],  # the default checkout form email is mandatory
#         source=request.form['stripeToken']
#     )
#
#     # charge object: https://stripe.com/docs/api/python#charges
#     # charge.amount  # ALWAYS in cents!
#     # charge.currency
#     # charge.description (the one you sent below in the dict)
#     # charge.outcome   object with payment acceptance details
#     # charge.paid
#     # charge.status ('succeeded')
#     charge = stripe.Charge.create(
#         customer=customer.id,
#         amount=amount,
#         currency=currency,
#         description='QGIS Donation'
#     )
#
#     return render_template('charge.html', amount=amount, currency=charge.currency, email=email)
