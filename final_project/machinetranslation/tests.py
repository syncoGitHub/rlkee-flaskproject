import unittest
from .translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):

    def testHelloToBonjour(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def testAxeToHache(self):
        self.assertEqual(englishToFrench("Telephone"), "Téléphone")

    def testNullToNull(self):
        with(self.assertRaises(Exception)):
            englishToFrench("")


class TestFrenchToEnglish(unittest.TestCase):

    def testBonjourToHello(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    def testHacheToAxe(self):
        self.assertEqual(frenchToEnglish("Téléphone"), "Telephone")

    def testNullToNull(self):
        with(self.assertRaises(Exception)):
            frenchToEnglish("")

unittest.main()