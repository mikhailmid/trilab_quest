import argparse
from typing import Optional

import requests
from requests.exceptions import RequestException


def get_gold_price(date: Optional[str]) -> Optional[float]:
    date = date or ""  # empty string if date=None
    api_url = f'https://api.nbp.pl/api/cenyzlota/{date}?format=json'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except RequestException as e:
        print(f'Error fetching data: {e}')
        return None
    else:
        gold_data = response.json()
        return gold_data[0]["cena"]


def main():
    parser = argparse.ArgumentParser(description='Get the gold price for a specific or today\'s date.')
    parser.add_argument('--date', help='Date in YYYY-MM-DD format (optional)')

    args = parser.parse_args()
    date = args.date

    gold_price = get_gold_price(date)

    if gold_price is not None:
        if date:
            print(f'Gold price on {date}: {gold_price} ZŁ per kg')
        else:
            print(f'Current gold price: {gold_price} ZŁ per kg')


if __name__ == '__main__':
    main()
