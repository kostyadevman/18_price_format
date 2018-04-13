import argparse
import re


def get_argument():
    parser = argparse.ArgumentParser('Price format')
    parser.add_argument('--price', type=str, required=True)
    return parser.parse_args()


def format_price(price):
    if not isinstance(price, (int, float, str)):
        raise TypeError
    if not re.match('^\d+\.?\d+$', str(price).strip(' ')):
        raise ValueError

    price = float(price)
    return '{:,.2f}'.format(price).replace(',', ' ').replace('.00', '')


if __name__ == '__main__':
    args = get_argument()
    print(format_price(args.price))
