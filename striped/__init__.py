from flask import Flask
from flask_cors import CORS
from striped import config
import stripe


app = Flask(__name__)
# CONFIGURATION
# See: http://flask.pocoo.org/docs/1.0/config/

# default config from config.default.py (or environment)
app.config.from_object(config.default)

cors = CORS(
    app,
    origins=app.config['CORS_ORIGINS']
)

# configuration (ini file type) overriding default config
# file should be in an 'instance' folder in application instance root
app.config.from_envvar('QGIS_STRIPED_SETTINGS', silent=True)

# or from an application.cfg (python file) 
app.config.from_pyfile('config/live.py', silent=True)

# set strip secret key
stripe.api_key = app.config['STRIPE_SECRET_KEY']

# Don't import actual view methods themselves - see:
# http://flask.pocoo.org/docs/patterns/packages/#larger-applications
# Also views must be imported AFTER app is created above.
# noinspection PyUnresolvedReferences
from striped import views
