# coding: utf-8

import unittest
import calculator

class CaluculatorTest(unittest.TestCase):

    def test__1(self): #normal case
        expected = -2
        actual = calculator.main('3-4/2*3+1')
        self.assertEqual(expected, actual)

    def test__2(self): #one number case
        expected = 0
        actual = calculator.main('0')
        self.assertEqual(expected, actual)

    def test__3(self): #fractional case
        expected = -1.9
        actual = calculator.main('3.0+4.5*0.2-5.8')
        self.assertEqual(expected, actual)

    def test__4(self): #dividing by 0 case
        with self.assertRaisesRegexp(Exception, 'Can not be divided by 0'):
            calculator.main('5+4/0')

    def test__5(self): #invalid syntax case
        with self.assertRaisesRegexp(Exception, 'Invalid syntax'):
            calculator.main('2+3/')

    def test__6(self): #invalid character case
        with self.assertRaisesRegexp(Exception, 'Invalid character found: :'):
            calculator.main('4+5:1')

    def test__7(self): #invalid character case
        # with self.assertRaises(Exception):
        with self.assertRaisesRegexp(Exception, 'Invalid syntax'):
            calculator.main('3+4-/5+1')

if __name__ == "__main__":
    unittest.main()
