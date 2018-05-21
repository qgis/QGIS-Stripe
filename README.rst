




Structure based on: https://github.com/kartoza/osm-reporter
and http://flask.pocoo.org/docs/1.0/patterns/packages/

From Flask Stripe integration: https://stripe.com/docs/checkout/flask

We’re creating a dictionary with Stripe’s tokens, publishable_key and secret_key which are being pulled out of the current environmental variables. We’re not hardcoding these keys, since it’s bad practice to put sensitive data into source control.

http://flask.pocoo.org/docs/1.0/config/

https://elasticcompute.io/2016/01/21/runtime-secrets-with-docker-containers/

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



Questions/Discussion:

- Ok to run gunicorn and use reverse proxy on Apache on qgis.org/stripe?

- Integration with website: button is easy, but how to handle callback / errors etc.
Separate page(s), but how to be translated?
Or a generic 'thankyou' page in sphinx, so Striped can redirect to that with
some extra info: in querystring?, via Callback? ...

- start with 5.00$ Button (Credit Card), then later more advanced forms?

- call back to Juergens scripts? Directly? Or via some api/callback?

# works to inject the button in a page
# prolem is the 'return' data? Redirect or inject again? Popup?
$.get( "http://localhost/stripe/", function( data ) {
  $( "#stripediv" ).html( data );
  console.log(data)
});

$.get( "https://duif.net/stripe/", function( data ) {
  $( "#paypal" ).html( data );
  console.log(data)
});

# testing for errors:
https://stripe.com/docs/testing#cards

    invalid_expiry_month: Use an invalid month (e.g., 13)
    invalid_expiry_year: Use a year in the past (e.g., 1970)
    invalid_cvc: Use a two digit number (e.g., 99)

