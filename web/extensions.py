from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_celery import Celery
from flask_babel import Babel
from flask_assets import Environment
from flask_mail import Mail

from web.models import User

# Setup flask cache
cache = Cache()

# Setup celery
celery = Celery()

# Setup Mail
mail = Mail()

# Setup Babel
babel = Babel()

# init flask assets
assets_env = Environment()

debug_toolbar = DebugToolbarExtension()

login_manager = LoginManager()
login_manager.login_view = "main.login"
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
