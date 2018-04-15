from format_price import format_price
import unittest


class FormatPriceTest(unittest.TestCase):
    def test_valid_str(self):
        self.assertEqual(format_price('3245.000000'), '3 245')

    def test_valid_int(self):
        self.assertEqual(format_price(567), '567')

    def test_valid_float(self):
        self.assertEqual(format_price(2750.476), '2 750.48')

    def test_invalid_string(self):
        self.assertEqual(format_price('1234a.17'), None)

    def test_invalid_str_2(self):
        self.assertEqual(format_price('1234,01'), None)

    def test_invalid_float(self):
        self.assertEqual(format_price(-999.04), None)

    def test_invalid_tuple(self):
        self.assertEqual(format_price((1234.00,)), None)

    def test_invalid_dict(self):
        self.assertEqual(format_price({1234}), None)

    def test_invalid_list(self):
        self.assertEqual(format_price([567.80]), None)


if __name__ == '__main__':
    unittest.main()
