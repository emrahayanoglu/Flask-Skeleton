from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from flask_babel import gettext, ngettext

from web.extensions import cache, mail
from web.forms import LoginForm
from web.models import User

from flask_mail import Message
from flask import current_app

main = Blueprint('main', __name__)


@main.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')


@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user)

        flash("Logged in successfully.", "success")
        return redirect(request.args.get("next") or url_for(".home"))

    return render_template("login.html", form=form)

@main.route("/lostpassword", methods=["GET", "POST"])
def lost_password():
    form = LostPasswordForm()
    if form.validate_on_submit():
        # mail = Mail(current_app)
        pass
    return render_template("lostpassword.html")

@main.route("/resetpassword", methods=["GET", "POST"])
def reset_password():
    form = ResetForm()
    if form.validate_on_submit():
        return redirect(url_for(".login"))

    return render_template("resetpassword.html")

@main.route("/logout")
def logout():
    logout_user()
    flash(gettext("You have been logged out."), "success")

    return redirect(url_for(".home"))


@main.route("/restricted")
@login_required
def restricted():
    return gettext("You can only see this if you are logged in!"), 200
