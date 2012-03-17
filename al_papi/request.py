import al_papi

class Request(object):
  """
    docstring for Request
  """
  @staticmethod
  def default_headers():
    return { 'Content-type': 'application/json' }
  
  def __init__(self):
    self.success = None
    self.errors  = []
  
  def post(self, params = {}):
    al_papi.AlHttp.post(params)
  
  def get(self, params = {}):
    al_papi.AlHttp.post(params)
