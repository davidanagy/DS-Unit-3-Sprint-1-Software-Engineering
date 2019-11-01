"""Generates random products and prints a summary"""

from acme import Product
from random import randint, uniform

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
COLORS = ['red', 'blue', 'black', 'white']


def generate_products(number=30):
    products = []
    for n in range(number):
        random1 = randint(0, 4)
        random2 = randint(0, 4)
        random_name = f'{ADJECTIVES[random1]} {NOUNS[random2]}'
        random_price = randint(5, 100)
        random_weight = randint(5, 100)
        random_flammability = uniform(0, 2.5)
        total_colors = randint(1, 4)
        random_colors = []
        for n in range(total_colors):
            random_color = randint(0, 3)
            random_colors.append(COLORS[random_color])
        prod = Product(
            random_name, random_price,
            random_weight, random_flammability, random_colors)
        products.append(prod)
    return products


def inventory_report(products):
    names = [prod.name for prod in products]
    prices = [prod.price for prod in products]
    weights = [prod.weight for prod in products]
    flames = [prod.flammability for prod in products]
    prod_colors = [prod.colors for prod in products]
    unique_names = list(set(names))
    mean_price = sum(prices) / len(prices)
    mean_weight = sum(weights) / len(weights)
    mean_flames = sum(flames) / len(flames)
    explosions = 0
    for prod in products:
        if prod.weight * prod.flammability >= 10:
            explosions += 1

    print(f'The number of unique names is {len(unique_names)}.')
    print(f'The average price is {mean_price}.')
    print(f'The average weight is {mean_weight}.')
    print(f'The average flammability is {mean_flames}.')
    print(f'There were {explosions} total explosions.')


if __name__ == '__main__':
    inventory_report(generate_products())
