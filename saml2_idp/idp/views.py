from flask import Flask, abort, redirect, request, session
from flask.views import MethodView
import logging
from .db import users


class Login(MethodView):
    def get(self):
        options = ''.join(f'<option value="{user.username}">{user.email}</option>'
                          for user in users.values())
        select = f'<div><label>Select a user: <select name="user">{options}</select></label></div>'

        next_url = request.args.get('next')
        next = f'<input type="hidden" name="next" value="{next_url}">'

        submit = '<div><input type="submit" value="Login"></div>'

        form = f'<form action="." method="post">{select}{next}{submit}</form>'
        header = '<title>Login</title><p>Please log in to continue.</p>'

        return header + form

    def post(self):
        user = request.form['user']
        next = request.form['next']

        session['user'] = user
        logging.info("Logged user", user, "in")
        logging.info("Redirecting to", next)

        return redirect(next)

