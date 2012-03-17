from tests.test_helper import *

class TestLocales(unittest.TestCase):
  
  def test_google_locales(self):
    assert_equal(Locales.supported(), Locales.google())
  
  def test_yahoo_locales(self):
    assert_equal(Locales.supported("yahoo"), Locales.yahoo())
  
  def test_bing_locales(self):
    assert_equal(Locales.supported("bing"), Locales.bing())