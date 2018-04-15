import argparse
import re


def get_argument():
    parser = argparse.ArgumentParser('Price format')
    parser.add_argument('--price', type=str, required=True)
    return parser.parse_args()


def format_price(price):
    if not isinstance(price, (int, float, str)):
        return None
    if not re.match('^\d+\.?\d+$', str(price).strip(' ')):
        return None

    price = float(price)
    return '{:,.2f}'.format(price).replace(',', ' ').replace('.00', '')


if __name__ == '__main__':
    args = get_argument()
    pretty_price = format_price(args.price)
    if pretty_price:
        print(pretty_price)
    else:
        print('The error has occured')
