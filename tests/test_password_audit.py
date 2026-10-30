import unittest
from password_audit import assess

class PasswordAuditTests(unittest.TestCase):
    def test_short_password_warned(self):
        self.assertTrue(any("12 characters" in x for x in assess("abc123")["findings"]))
    def test_common_password_detected(self):
        self.assertTrue(any("common" in x for x in assess("password123")["findings"]))
    def test_empty_password(self):
        self.assertEqual(assess("")["length"],0)
if __name__ == "__main__": unittest.main()
