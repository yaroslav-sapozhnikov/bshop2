class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@localhost/bbsh'
    SECRET_KEY = '4321'
    
    
    SECURITY_PASSWORD_SALT = 'salt'
    SECORITY_PASSWORD_HASH = 'bcrypt'
    