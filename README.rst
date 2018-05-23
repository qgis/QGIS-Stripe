

QGIS-Stripe
-----------

QGIS-Stripe is a container which runs a small Flask application to:
- serve a test page (to do Test Stripe Payments)
- serve a dynamic form, to be injected (JQuery) into the QGIS Donation webpage
- serve a flask app which 1) handles Credit Card payment 2) returns a result json

Running
-------

For production use, you should clone this app (/var/www/github on qgis2)

(re)Build the container::

 docker-compose build

IF in production mode, make sure there is a live.py configuration in striped/config
Run the container::

 docker-compose up

Deamonize::

 docker-compose up -d

Stop::

 docker-compose stop

Start it again::

 docker-compose up -d


Development
-----------


For Flask info http://flask.pocoo.org/docs/1.0/patterns/packages/

For Flask configuration info: http://flask.pocoo.org/docs/1.0/config/

For Stripe integration: https://stripe.com/docs/checkout/flask


For development it is easiest to use the 'runserver.py':
- clone this repo
- ...

Works to inject the button in a page (site contains JQuery as $) ::

 $.get( "http://localhost/stripe/", function( data ) {
   $( "#stripediv" ).html( data );
   console.log(data)
 });

If you want to test production keys, you HAVE TO server from https page::

 $.get( "https://duif.net/stripe/", function( data ) {
   $( "#paypal" ).html( data );
   console.log(data)
 });



https://elasticcompute.io/2016/01/21/runtime-secrets-with-docker-containers/

Stripe Test keys are in config/default.py

https://stripe.com/docs/testing#cards

Stripe Test CreditCardNumber: 4242 4242 4242 4242
And valid date in future and arbitrary 3 digit cvc number


Testing for errors:
- invalid_expiry_month: Use an invalid month (e.g., 13)
- invalid_expiry_year: Use a year in the past (e.g., 1970)
- invalid_cvc: Use a two digit number (e.g., 99)
