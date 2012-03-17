from tests.test_helper import *

class TestConfig(unittest.TestCase):
    
    def setUp(self):
      self.config = Config("api-key")
    
    def test_default_host(self):
      assert_equal("http://api.authoritylabs.com", self.config.default_host)
    
    def test_default_port(self):
      assert_equal(80, self.config.port)
    
    def test_setup(self):
      Config.setup("my-api-key")
      assert_equal("my-api-key", Config.api_key)