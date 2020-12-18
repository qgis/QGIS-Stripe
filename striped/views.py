from striped import app
from flask import render_template, request, redirect, jsonify, url_for, json
import stripe


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    content = request.json
    donation_name = 'Donation'
    donation_quantity = 1
    donation_amount = int(content['donationAmount'])
    donation_currency = content['donationCurrency']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': donation_currency,
                'product_data': {
                    'name': donation_name,
                },
                'unit_amount': donation_amount,
            },
            'quantity': donation_quantity,
        }],
        mode='payment',
        success_url='{}?payment_success=True'.format(
            app.config['QGIS_DONATION_URL']),
        cancel_url=app.config['QGIS_DONATION_URL']
    )
    return jsonify(id=session.id)


@app.route('/')
def index():
    return redirect(app.config['QGIS_DONATION_URL'], code=302)


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
                           recaptcha_key=app.config['GOOGLE_RECAPTCHA_KEY'],
                           stripecheckouturl=app.config['STRIPE_CHECKOUT_URL'])
