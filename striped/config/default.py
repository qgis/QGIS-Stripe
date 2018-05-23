# -*- coding:utf-8 -*-
"""Configuration options for the striped app.
:copyright: (c) 2018 Richard Duivenvoorde
:license: GPLv3, see LICENSE for more details.
"""
import os

# Stripe PUBLISHABLE_KEY (offical Stripe TEST key)
STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY') \
    if os.environ.get('STRIPE_PUBLISHABLE_KEY', False) else \
    'pk_test_6pRNASCoBOKtIshFeQd4XMUh'

# Stripe SECRET_KEY (offical Stripe TEST key)
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY') \
    if os.environ.get('STRIPE_SECRET_KEY', False) else \
    'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

STRIPE_FORM_URL = os.environ.get('STRIPE_FORM_URL') \
    if os.environ.get('STRIPE_FORM_URL', False) else \
    '/stripe/form'

STRIPE_CHARGE_URL = os.environ.get('STRIPE_CHARGE_URL') \
    if os.environ.get('STRIPE_CHARGE_URL', False) else \
    '/stripe/chargejson'
