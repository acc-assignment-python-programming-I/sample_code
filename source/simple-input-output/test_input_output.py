import unittest
from input_output import process_input


class TestMain(unittest.TestCase):
    def test_process_input(self):
        """
        Test the process_input function.
        """
        self.assertEqual(process_input("test"), "You entered: test")
        self.assertEqual(process_input("123"), "You entered: 123")
        self.assertEqual(process_input(""), "You entered: ")


if __name__ == '__main__':
    unittest.main()
