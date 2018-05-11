from flask import Flask
import os
import stripe
from striped.config import default

# stripe_keys = {
#   'secret_key': os.environ['SECRET_KEY'],
#   'publishable_key': os.environ['PUBLISHABLE_KEY']
# }

# TODO: make this come form environment or config files
stripe_keys = {
  'secret_key': 'sk_test_BQokikJOvBiI2HlWgH4olfQ2',
  'publishable_key': 'pk_test_6pRNASCoBOKtIshFeQd4XMUh'
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)
# Don't import actual view methods themselves - see:
# http://flask.pocoo.org/docs/patterns/packages/#larger-applications
# Also views must be imported AFTER app is created above.
# noinspection PyUnresolvedReferences
from striped import views
