"""Defines the 'product' class and related subclasses"""

from random import randint


class Product:
    """general representation of acme products"""
    identifier = randint(1000000, 9999999)

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def stealability(self):
        steal = self.price / self.weight
        if steal < 0.5:
            return 'Not so stealable...'
        elif steal >= 0.5 and steal < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        explode = self.flammability * self.weight
        if explode < 10:
            return '...fizzle.'
        if explode >= 10 and explode < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    """
    Boxing gloves, subclass of Product
    """
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
