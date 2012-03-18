import al_papi

class Response(object):
  """
    docstring for Response
  """
  
  def __init__(self, req, path, params):
    self.success = req.success
    self.code    = req.code
    self.body    = req.body
    self.errors  = req.errors
    self.params  = params
    self.path    = path
    self.code    = req.code
  
  