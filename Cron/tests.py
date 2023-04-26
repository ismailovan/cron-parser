import unittest
from cron import Cron

class TestCron(unittest.TestCase):
    def test0(self):
        cr = Cron('*/15 0 1,15 * 1-5 /usr/bin/find')
        self.assertEqual(cr.minute, [0, 15, 30, 45])
        self.assertEqual(cr.hour, [0])
        self.assertEqual(cr.day, [1, 15])
        self.assertEqual(cr.month, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(cr.day_w, [1, 2, 3, 4, 5])
    
    def test1(self):
        cr = Cron('1-30/6,12-29/4,31-31/1 0,2,5,6,1,7 1-15/10 * 1-7 /usr/bin/find')
        self.assertEqual(cr.minute, [1, 7, 12, 13, 16, 19, 20, 24, 25, 28, 31])
        self.assertEqual(cr.hour, [0, 1, 2, 5, 6, 7])
        self.assertEqual(cr.day, [1, 11])
        self.assertEqual(cr.month, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(cr.day_w, [1, 2, 3, 4, 5, 6, 7])
    
    def test2(self):
        cr = Cron('0 23 1,15-18,12-22/3 */3 2 /usr/bin/find')
        self.assertEqual(cr.minute, [0])
        self.assertEqual(cr.hour, [23])
        self.assertEqual(cr.day, [1, 12, 15, 16, 17, 18, 21])
        self.assertEqual(cr.month, [1, 4, 7, 10])
        self.assertEqual(cr.day_w, [2])
    
if __name__ == '__main__':
    unittest.main()
