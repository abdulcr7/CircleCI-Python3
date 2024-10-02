import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "AbdulCR7" 
        up = to_upper(name)
        self.assertEqual(up, "ABDULCR7")  # Changed expected output to uppercase

if __name__ == '__main__':
    unittest.main()
