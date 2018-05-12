
Structure based on: https://github.com/kartoza/osm-reporter
and http://flask.pocoo.org/docs/1.0/patterns/packages/

From Flask Stripe integration: https://stripe.com/docs/checkout/flask

We’re creating a dictionary with Stripe’s tokens, publishable_key and secret_key which are being pulled out of the current environmental variables. We’re not hardcoding these keys, since it’s bad practice to put sensitive data into source control.

Stripe Test keys:

PUBLISHABLE_KEY=pk_test_6pRNASCoBOKtIshFeQd4XMUh
SECRET_KEY=sk_test_BQokikJOvBiI2HlWgH4olfQ2

Stripe Test CreditCardNumber: 4242 4242 4242 4242

# works:
docker run -p 8000:8000 qgisstripe_web

# also works:
docker-compose up

# deamonize:
docker-compose up -d

# stop:
docker-compose stop
# start it again
docker-compose up -d


