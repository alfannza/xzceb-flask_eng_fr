import unittest
from machinetranslation.translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(""), "")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(""), "")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

unittest.main()

