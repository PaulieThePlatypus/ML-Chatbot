import unittest
from app import app

class TestHomeRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

if __name__ == '__main__':
    unittest.main()
