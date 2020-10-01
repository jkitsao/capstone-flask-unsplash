import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'pepe'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/splash'
    SQLALCHEMY_TRACK_MODIFICATIONS =True


    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/splash'

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,

}
