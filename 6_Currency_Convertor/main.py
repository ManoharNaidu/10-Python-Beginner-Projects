import json
from typing import Union, Dict

def load_rates(json_file: str) -> Dict[str, Dict[str, Union[str, float]]]:
    with open(json_file, 'r') as file:
        return json.load(file)

def convert(amount: float, base: str, to: str, rates: Dict[str, Dict[str, Union[str, float]]]) -> float:
    base = base.lower()
    to = to.lower()

    from_rate = rates.get(base)
    to_rate = rates.get(to)

    if from_rate is None and base != 'eur':
        return -1
    if to_rate is None and to != 'eur':
        return -2

    if base == 'eur':
        return amount * to_rate['rate']
    elif to == 'eur':
        return amount / from_rate['rate']
    else:
        return amount / from_rate['rate'] * to_rate['rate']

def display_valid_currencies(rates: Dict[str, Dict[str, Union[str, float]]]) -> None:
    print("Valid currency options:")
    for currency in rates.keys():
        print(currency.upper())

def main() -> None:
    rates = load_rates('rates.json')
    display_valid_currencies(rates)
    base = input('From: ')
    to = input('To: ')
    amount = float(input('Amount: '))
    results = convert(amount, base, to, rates)
    if results == -1:
        print('Invalid base currency code. Please check the "base" currency code.')
        display_valid_currencies(rates)
    elif results == -2:
        print('Invalid target currency code. Please check the "to" currency code.')
        display_valid_currencies(rates)
    else:
        print(f"{amount} {base.upper()} is {results} {to.upper()}")

if __name__ == "__main__":
    main()