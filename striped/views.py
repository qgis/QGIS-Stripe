import stripe
import requests
from flask import render_template, request, redirect, jsonify, abort, json
from striped import app


def _verify_recaptcha(token):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    post_data = {
        'secret': app.config['GOOGLE_RECAPTCHA_SECRET_KEY'],
        'response': token
    }
    response = requests.post(url, data=post_data)
    response_obj = json.loads(response.text)
    if not response_obj['success']:
        abort(400, description='Illegal captcha request')


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    content = request.json
    donation_name = 'Donation'
    donation_quantity = 1
    donation_amount = int(content['donationAmount'])
    donation_currency = content['donationCurrency']
    recaptcha_token = content['recaptchaToken']

    _verify_recaptcha(recaptcha_token)

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


@app.errorhandler(400)
def custom400(error):
    response = jsonify({'message': error.description})
    response.status_code = 400
    response.status = error.description
    return response


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
                           donation_url=app.config['QGIS_DONATION_URL'],
                           stripecheckouturl=app.config['STRIPE_CHECKOUT_URL'])
