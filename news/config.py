import os


class config:
    """
    parent class configuration
    """
    


class ProdConfig(config):
    """
    production class configuration
    """
    pass


class DevConfig(config):
    """
    development class configuration
    """
    DEBUG = True


config_options = {
    'development': DevConfig,
    'Production': DevConfig
}
