from format_price import format_price
import unittest


class FormatPriceTest(unittest.TestCase):
    def test_valid_str(self):
        self.assertEqual(format_price('3245.000000'), '3 245')

    def test_valid_int(self):
        self.assertEqual(format_price(567), '567')

    def test_valid_float(self):
        self.assertEqual(format_price(2750.476), '2 750.48')

    def test_invalid_str(self):
        with self.assertRaises(ValueError):
            format_price('1234a.17')

    def test_invalid_str_2(self):
        with self.assertRaises(ValueError):
            format_price('1234,01')

    def test_invalid_float(self):
        with self.assertRaises(ValueError):
            format_price(-999.04)

    def test_invalist_type(self):
        with self.assertRaises(TypeError):
            format_price((1234.00,))


if __name__ == '__main__':
    unittest.main()
