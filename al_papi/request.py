import al_papi
from httplib2 import Http
from urllib import urlencode

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
    http = Http()
    params.update( { "auth_token" : al_papi.Config.api_key } )
    url = '%s/keywords.json?%s' % ( al_papi.Config.default_host, urlencode(params) )
    resp, content = http.request(url, "POST", headers=al_papi.Request.default_headers())
    print "RESPONSE"
    print resp
    print "CONTENT"
    print content
    
  def get(self, params = {}):
    http = Http()
    params.update( { "auth_token" : al_papi.Config.api_key } )
    url = '%s/keywords/get.json?%s' % ( al_papi.Config.default_host, urlencode(params) )
    resp, content = http.request(url, "GET", headers=al_papi.Request.default_headers())
    print "RESPONSE"
    print resp
    print "CONTENT"
    print content
    
  