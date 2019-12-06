from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
from flask_babel import gettext
from flask_login import login_user, login_required, logout_user
from itsdangerous import URLSafeSerializer, BadSignature
from app.extensions import lm
from app.jobs import send_registration_email
from app.user.models import User
from app.user.forms import RegisterUserForm
from .forms import LoginForm
from ..auth import auth



@auth.route('/prihlaseni', methods=['GET', 'POST'])
def prihlaseni():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        flash(
            gettext(
                'You were logged in as {username}'.format(
                    username=form.user.username
                ),
            ),
            'success'
        )
        return redirect(request.args.get('next') or url_for('index'))
    return render_template('login.html', form=form)



