"""Generates random products and prints a summary"""

from acme import Product
from random import randint, uniform

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(number=30):
    products = []
    for n in range(number):
        random1 = randint(0, 4)
        random2 = randint(0, 4)
        random_name = f'{ADJECTIVES[random1]} {NOUNS[random2]}'
        random_price = randint(5, 100)
        random_weight = randint(5, 100)
        random_flammability = uniform(0, 2.5)
        prod = Product(
            random_name, random_price,
            random_weight, random_flammability)
        products.append(prod)
    return products


def inventory_report(products):
    names = [prod.name for prod in products]
    prices = [prod.price for prod in products]
    weights = [prod.weight for prod in products]
    flames = [prod.flammability for prod in products]
    unique_names = list(set(names))
    mean_price = sum(prices) / len(prices)
    mean_weight = sum(weights) / len(weights)
    mean_flames = sum(flames) / len(flames)
    print(f'The number of unique names is {len(unique_names)}.')
    print(f'The average price is {mean_price}.')
    print(f'The average weight is {mean_weight}.')
    print(f'The average flammability is {mean_flames}.')


if __name__ == '__main__':
    inventory_report(generate_products())
