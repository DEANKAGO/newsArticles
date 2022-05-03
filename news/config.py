import os

class config:
  """
  parent class configuration
  """
  NEWS_API_KEY =  os.environ.get('79f4f137ac6749fa9f5fa076e9336883')
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=79f4f137ac6749fa9f5fa076e9336883'

class ProdConfig(config):
  pass  

class DevConfig(config):
  DEBUG= True

config_options = {
  'development':DevConfig,
  'Production':DevConfig
}