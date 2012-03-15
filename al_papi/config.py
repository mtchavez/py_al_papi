import al_papi

class Config(object):
  """
    Config class for storing credentials for request.
  """
  default_host = "http://api.authoritylabs.com"
  port         = 80
  
  def __init__(self, api_key):
    self.api_key = api_key
  
