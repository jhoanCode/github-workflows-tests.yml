import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode(), '¡Hola, mundo! Esta es una aplicación web simple.')

if __name__ == '__main__':
    unittest.main()
