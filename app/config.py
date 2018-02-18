import os


class Config(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/carp_development'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('CARP_DATABASE_URI')


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.getenv('CARP_DATABASE_URI')


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/carp_test'


config = {
    'production': ProductionConfig,
    'staging': StagingConfig,
    'development': DevelopmentConfig,
    'test': TestConfig
}