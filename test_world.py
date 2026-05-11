
"""
class for testing pylint
"""

import unittest
import olo

class Text(unittest.testcase):
    """
    class for testing pylint
    """

    def test_one_word(self):
        """
        class for testing pylint
        """
        text = 'python'
        result = olo.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiple_word(self):
        """
        class for testing pylint
        """
        text ='rohan naughty'
        result = olo.cap_text(text)
        self.assertEqual(result,'Rohan Naughty')
if __name__=='__main__':
    unittest.main()
