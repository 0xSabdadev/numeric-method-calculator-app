class Config(object):
    DEBUG = False
    TESTING = False

    # SECRET_KEY = "@12Y454LS4I3IL4"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True