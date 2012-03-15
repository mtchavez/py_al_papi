from tests.test_helper import *

class TestEngines(unittest.TestCase):

  def test_all_engines(self):
    assert_equal(Engines.all(), ["google", "yahoo", "bing"])
    