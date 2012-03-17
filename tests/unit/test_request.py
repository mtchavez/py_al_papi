from tests.test_helper import *

class TestRequest(unittest.TestCase):
  
  def test_init_sets_success(self):
    assert_equal(Request().success, None)
  
  def test_init_sets_errors(self):
    assert_equal(Request().errors, [])
  
  @unittest.skip("Figure out test with http requests")
  def testPost(self):
    assert_true()
  