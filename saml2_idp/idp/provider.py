from flask import abort, redirect, request, session, url_for
from flask_saml2.idp import IdentityProvider
from .db import users


class BTIdentityProvider(IdentityProvider):
    def login_required(self):
        if not self.is_user_logged_in():
            next = url_for('login', next=request.url)
            abort(redirect(next))

    def is_user_logged_in(self):
        return 'user' in session and session['user'] in users

    def logout(self):
        del session['user']

    def get_current_user(self):
        return users[session['user']]
