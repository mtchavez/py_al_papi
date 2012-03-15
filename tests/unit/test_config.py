from tests.test_helper import *

class TestConfig(unittest.TestCase):
    
    def setUp(self):
      self.config = Config("api-key")
    
    def test_default_host(self):
        assert_equal("http://api.authoritylabs.com", self.config.default_host)
    
    def test_default_port(self):
        assert_equal(80, self.config.port)
    