import unittest
import VolumeOfCube

voc = VolumeOfCube
class testCases(unittest.TestCase):
    def integer_test(self):
        self.assertEqual(voc.findVolume(5), 125)
    def float_test(self):
        self.assertEqual(voc.findVolume(5.2), 140.608)
    def negative_test(self):
        self.assertEqual(voc.findVolume(-4), -1)
if __name__ == '__main__':
    unittest.main(verbosity=2)