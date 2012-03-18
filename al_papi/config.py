import al_papi

class Config(object):
  """
    Config class for storing credentials for request.
  """
  default_host = "http://api.authoritylabs.com"
  port         = 80
  api_key      = ""

  @staticmethod
  def setup(api_key):
    Config.api_key = api_key

  @staticmethod
  def create():
    return Config(Config.api_key)

  def __init__(self, api_key):
    self.api_key = api_key
  
