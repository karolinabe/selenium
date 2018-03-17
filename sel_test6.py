import unittest
from selenium import webdriver



class SampleTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()



        # Wywoływana przed każdym testem
        pass

    def tearDown(self):
        self.driver.quit()
        # Wywoływana po każdym teście
        pass

    def test_first(self):
        self.driver.get("https://pl.wikipedia.org")
        self.assertEqual(1, 1)

    def test_second(self):
        self.driver.get("https://www.google.com")
        self.assertListEqual(["a", "b"], ["a", "b"])
