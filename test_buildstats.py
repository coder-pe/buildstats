import unittest

from datacapture import DataCapture

class TestBuildStats(unittest.TestCase):
    
    def setUp(self):
        ### given three elements
        self.data_capture = DataCapture()
        self.data_capture.add(20)
        self.data_capture.add(32)
        self.data_capture.add(12)
        
        self.build_stats = self.data_capture.build_stats()
    
    def tearDown(self):
        pass
    
    def test_less(self):
        ### when less medium data should return low values
        result = self.build_stats.less(20)
        expected = [12]
        
        self.assertEqual(result, expected)
        
        ### when less than lowest data should return empty list
        result = self.build_stats.less(12)
        expected = []
        
        self.assertEqual(result, expected)
        
        ### when less than highest data should return all values
        result = self.build_stats.less(40)
        expected = [12, 20, 32]
        
        self.assertEqual(result, expected)
    
    def test_between(self):
        ### when get data between lowest and highest
        result = self.build_stats.between(12, 32)
        expected = [20]
        
        self.assertEqual(result, expected)
        
    def test_greater(self):
        ### when greater medium data should return higher values
        result = self.build_stats.greater(20)
        expected = [32]
        
        self.assertEqual(result, expected)
        
        ### when greater than lowest data should return higher values
        result = self.build_stats.greater(12)
        expected = [20, 32]
        
        self.assertEqual(result, expected)
        
        ### when greater than highest data should return empty list
        result = self.build_stats.greater(32)
        expected = []
        
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
