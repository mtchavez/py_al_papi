import al_papi

class Request(object):
  """
    docstring for Request
  """
  
  @staticmethod
  def post(params = {}, priority = False):
    return al_papi.AlHttp.post(params, priority)
  
  @staticmethod
  def priority_post(params = {}, priority = False):
    return al_papi.AlHttp.priority_post(params)
  
  @staticmethod
  def get(params = {}):
    return al_papi.AlHttp.get(params)
  
