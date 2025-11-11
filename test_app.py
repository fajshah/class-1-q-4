import unittest
import json
from app import app

class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_calculate_addition(self):
        response = self.app.post('/calculate',
                                 data=json.dumps({'expression': '2+3'}),
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 5)

    def test_calculate_subtraction(self):
        response = self.app.post('/calculate',
                                 data=json.dumps({'expression': '5-3'}),
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 2)

    def test_calculate_multiplication(self):
        response = self.app.post('/calculate',
                                 data=json.dumps({'expression': '2*3'}),
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 6)

    def test_calculate_division(self):
        response = self.app.post('/calculate',
                                 data=json.dumps({'expression': '6/3'}),
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 2)

    def test_calculate_invalid_expression(self):
        response = self.app.post('/calculate',
                                 data=json.dumps({'expression': '2+'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_calculate_sin(self):
        response = self.app.post('/calculate',
                                 data=json.dumps({'expression': 'sin(0)'}),
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 0)

if __name__ == '__main__':
    unittest.main()
