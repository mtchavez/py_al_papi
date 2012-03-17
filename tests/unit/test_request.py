from tests.test_helper import *

class TestRequest(unittest.TestCase):
  
  def testInitSuccess(self):
    assert_equal(Request().success, None)
  
  def testInitErrors(self):
    assert_equal(Request().errors, [])
  
  @unittest.skip("Figure out test with http requests")
  def testPost(self):
    assert_true()
  