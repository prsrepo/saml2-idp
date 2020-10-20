#!/usr/bin/env python3
import logging
import os

from flask import Flask
from saml2_idp.idp.views import Login
from saml2_idp.idp.provider import BTIdentityProvider
from saml2_idp.certificates import CERTIFICATE, PRIVATE_KEY
from saml2_idp.sp.providers import SAML2_SERVICE_PROVIDERS

logger = logging.getLogger(__name__)


def get_wsgi_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("IDP_SECRET", 'WUGYGOIH97897yu$@876rfg7iujfFTD')
    app.config['SERVER_NAME'] = 'pr.localhost.com:8001'
    app.config['SAML2_IDP'] = {
        'autosubmit': True,
        'certificate': CERTIFICATE,
        'private_key': PRIVATE_KEY,
    }
    app.config['SAML2_SERVICE_PROVIDERS'] = SAML2_SERVICE_PROVIDERS
    app.add_url_rule('/login/', view_func=Login.as_view('login'))
    app.register_blueprint(BTIdentityProvider().create_blueprint(), url_prefix='/saml/')

    return app
