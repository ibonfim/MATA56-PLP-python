import unittest
from datetime import datetime, timedelta

class TestDatetimeUtils(unittest.TestCase):
    def test_timedelta_creation(self):
        delta = timedelta(days=1)
        self.assertEqual(delta.days, 1)
        self.assertEqual(delta.seconds, 0)
        
    def test_datetime_arithmetic(self):
        now = datetime.now()
        one_day = timedelta(days=1)
        tomorrow = now + one_day
        self.assertEqual(tomorrow - now, one_day)
        
    def test_negative_timedelta(self):
        delta = timedelta(days=-5)
        self.assertEqual(delta.days, -5)
        
    def test_timedelta_zero(self):
        delta = timedelta()
        self.assertEqual(delta.days, 0)
        self.assertEqual(delta.seconds, 0)
        
    def test_timedelta_microseconds(self):
        delta = timedelta(microseconds=1000)
        self.assertEqual(delta.microseconds, 1000)
        
    def test_timedelta_comparison(self):
        delta1 = timedelta(days=1)
        delta2 = timedelta(hours=24)
        self.assertEqual(delta1, delta2)
        
if __name__ == '__main__':
    unittest.main()
