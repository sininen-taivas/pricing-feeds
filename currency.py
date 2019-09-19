#!/usr/bin/env python3
from argparse import ArgumentParser

import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen

URL = 'https://api.coingecko.com/api/v3/coins/ergo?localization=false&tickers=true&market_data=true&community_data=false&developer_data=false&sparkline=false'

def get_currency(currency):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    req = Request(url=URL, headers=headers)
    res = urlopen(req)  # type: http.client.HTTPResponse
    data = json.loads(res.read())
    price = data.get('market_data',{}).get('current_price',{}).get(currency)

    return price


def parse_cli():
    parser = ArgumentParser(description='Retrieves price ergo-token in fiat currency')
    parser.add_argument('currency', nargs='?', const=1, type=str, default='usd', help='currency short name')
    opts = parser.parse_args()
    return opts


def main():
    opts = parse_cli()
    print(get_currency(opts.currency))


if __name__ == '__main__':
    main()
