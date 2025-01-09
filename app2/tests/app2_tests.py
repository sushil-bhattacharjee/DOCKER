import unittest
import requests
import re 

class AppTest(unittest.TestCase):
    
    def setUp(self):
        self.url = 'http://10.1.10.98:9500'
        
    def test_welcome(self):
        response = requests.get(self.url)
        status_code = response.status_code
        content = response.content.decode('ascii')
        
        self.assertEqual(status_code, 200)
        self.assertIn('Welcome to Cisco DevNet!', content)
        
    def test_welcome_negative(self):
        response = requests.get(self.url)
        status_code = response.status_code
        content = response.content.decode('ascii')
        
        self.assertEqual(status_code, 200)
        self.assertNotIn('Welcome home.', content)
        
    def test_ip(self):
        response = requests.get(self.url)
        status_code = response.status_code
        content = response.content.decode('ascii')
        
        self.assertEqual(status_code, 200)
        ip_regex = r"IP Address of the server is ([0-9]{1,3}\.){3}[0-9]{1,3}."
        self.assertRegex(content, re.compile(ip_regex, re.IGNORECASE))  # Use re.IGNORECASE to match case-insensitively
        
if __name__ == '__main__':
    unittest.main()