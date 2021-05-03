import unittest
import fullName


class testCases(unittest.TestCase):
    def fullName_test(self):
        self.assertEqual(fullName.compoundName("John", "Smith"), "John Smith")
    def lastName_test(self):
        self.assertEqual(fullName.compoundName("", "Smith"), -1)
    def firstName_test(self):
        self.assertEqual(fullName.compoundName("John", ""), -1)

if __name__ == '__main__':
    unittest.main(verbosity=2)