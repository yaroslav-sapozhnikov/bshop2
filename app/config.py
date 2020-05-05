class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@localhost/bbsh'
    SECRET_KEY = '4321'

    MAIL_USERNAME = 'flaskapp726@gmail.com'
    MAIL_PASSWORD = '123456flask'
    MAIL_DEFAULT_SENDER = '"MyApp" <flaskapp726@gmail.com>'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = '465'
    MAIL_USE_SSL = True

    SECURITY_CONFIRMABLE = True
    SECURITY_EMAIL_SENDER = 'flaskapp726@gmail.com'

    SECURITY_RECOVERABLE = True
    SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = True

    SECURITY_REGISTERABLE = True


    # Flask-User settings
    USER_APP_NAME = "AppName"  # Used by email templates
    
    
    SECURITY_PASSWORD_SALT = 'salt'
    SECORITY_PASSWORD_HASH = 'bcrypt'
    