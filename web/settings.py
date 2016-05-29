import tempfile
db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = 'REPLACE ME'


class ProdConfig(Config):
    ENV = 'prod'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    CACHE_TYPE = 'simple'

    MAIL_SERVER = "email-smtp.us-east-1.amazonaws.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "your aws username"
    MAIL_PASSWORD = "your aws password"
    MAIL_DEFAULT_SENDER = "your default sender mail"


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    CACHE_TYPE = 'null'
    ASSETS_DEBUG = True

    MAIL_SERVER = "email-smtp.us-east-1.amazonaws.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "your aws username"
    MAIL_PASSWORD = "your aws password"
    MAIL_DEFAULT_SENDER = "your default sender mail"


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file.name
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False

    MAIL_SERVER = "email-smtp.us-east-1.amazonaws.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "your aws username"
    MAIL_PASSWORD = "your aws password"
    MAIL_DEFAULT_SENDER = "your default sender mail"
