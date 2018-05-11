# -*- coding:utf-8 -*-
"""Configuration options for the striped app.
:copyright: (c) 2018 Richard Duivenvoorde
:license: GPLv3, see LICENSE for more details.
"""
import os

# Stripe PUBLISHABLE_KEY
PUBLISHABLE_KEY = os.environ.get('PUBLISHABLE_KEY') \
    if os.environ.get('PUBLISHABLE_KEY', False) else \
    'pk_test_6pRNASCoBOKtIshFeQd4XMUh'

# Stripe SECRET_KEY
SECRET_KEY = os.environ.get('SECRET_KEY') \
    if os.environ.get('SECRET_KEY', False) else \
    'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
