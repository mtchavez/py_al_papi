import al_papi

class RequestError(object):
  """
    docstring for RequestError
  """
  def __init__(self, message, code):
    self.message = message
    self.code    = code
    