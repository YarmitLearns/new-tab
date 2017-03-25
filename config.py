import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp-mail.outlook.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'yarmitporys@outlook.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    NEWTAB_MAIL_SUBJECT_PREFIX = '[New-Tab]'
    # after i confirm that this works, try to send a message as:
    # FLASKY_MAIL_SENDER = 'New-Tab Admin <yarmitporys@outlook.com>'
    NEWTAB_MAIL_SENDER = 'yarmitporys@outlook.com'
    # where is this used?
    NEWTAB_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'newtabTEST.db')
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username="newtab",
        password="My7349pass",
        hostname="newtab.mysql.pythonanywhere-services.com",
        databasename="newtab$default")

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}