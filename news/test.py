import unittest
from request import Request
from app import App 

class Testapp(unittest.TestCase):
  def test_create_app(self):
    """
    test if app is created
    """
    self.assertEqual(self.create_app)

  def test_configure_request(self):
    """
    test if request is configured
    """
    self.assertEqual(self.configure_request)

  def test_get_news(self):
    """
    test if request is configured
    """
    self.assertEqual(self.get_news)


if __name__ == '__main__':
  unittest.main()