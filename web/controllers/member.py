from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required

from web.extensions import cache, mail
from web.forms import LoginForm
from web.models import User

from flask_mail import Message
from flask import current_app

member = Blueprint('member', __name__)


@member.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!", 200
