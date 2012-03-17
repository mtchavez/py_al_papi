import al_papi

from httplib2 import Http
from urllib import urlencode

class AlHttp(object):
  """
    docstring for ClassName
  """
  
  post_path     = "/keywords.json"
  get_path      = "/keywords/get.json"
  priority_path = "/keywords/priority.json"
  
  @staticmethod
  def post(params = {}, priority = False):
    path = al_papi.AlHttp.post_path if priority == False else al_papi.AlHttp.priority_path
    al_papi.AlHttp.request("POST", params, path)
  
  def priority_post(params = {}):
    al_papi.AlHttp.request("POST", params, al_papi.AlHttp.priority_path)
  
  @staticmethod
  def request(verb, params, path):
    http = Http()
    params.update( { "auth_token" : al_papi.Config.api_key } )
    url = '%s%s?%s' % ( al_papi.Config.default_host, path, urlencode(params) )
    resp, content = http.request(url, verb, headers=al_papi.Request.default_headers())
    print "RESPONSE"
    print resp
    print "CONTENT"
    print content
    