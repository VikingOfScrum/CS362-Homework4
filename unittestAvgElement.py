import unittest
import ElementsList

el = ElementsList
class testCases(unittest.TestCase):
    def mean_test(self):
        self.assertEqual(el.AvgElement([1, 3, 5]), 3)
    def error_test(self):
        self.assertEqual(el.AvgElement([]), -1)
    def small_test(self):
        self.assertEqual(el.AvgElement([99]), 99)

if __name__ == '__main__':
    unittest.main(verbosity=2)