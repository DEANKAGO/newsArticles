import os


class config:
    """
    parent class configuration
    """
    


class ProdConfig(config):
    pass


class DevConfig(config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'Production': DevConfig
}
