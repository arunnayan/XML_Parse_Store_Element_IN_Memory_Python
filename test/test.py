from parser.xmlparser import XMLParser
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.ff = XMLParser(
            "../resources/xmltest.xml")

    # Returns True or False.
    def test(self):
        x = self.ff.getElementByXpath("//*[@version='2.0']")
        test = self.ff.getStorElementWithKey(x)
        self.assertIsNotNone(test)


if __name__ == '__main__':
    unittest.main()
