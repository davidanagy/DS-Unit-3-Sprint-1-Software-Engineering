"""Defines the 'product' class and related subclasses"""

from random import randint


class Product:
    """general representation of acme products"""
    identifier = randint(1000000, 9999999)

    def __init__(self, name, price=10, weight=20,
                 flammability=0.5, colors=['red']):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.colors = colors

    def stealability(self):
        """determines how stealable the product is"""
        steal = self.price / self.weight
        if steal < 0.5:
            return 'Not so stealable...'
        elif steal >= 0.5 and steal < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        """sees if the product explodes!"""
        explode = self.flammability * self.weight
        if explode < 10:
            return '...fizzle.'
        if explode >= 10 and explode < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

    def paint(self, color):
        """re-paints the produt to a different color"""
        self.colors = [color]
        return f'Re-painting to make it {color}! Ooh, shiny!'

    def add_color(self, color):
        """adds a color to the prodct"""
        self.colors.append(color)
        return f"Let's add {color}! It looks nice!"


class BoxingGlove(Product):
    """
    Boxing gloves, subclass of Product
    """
    def __init__(self, name, price=10, weight=10):
        super().__init__(name, price, weight)

    def explode(self):
        """gloves can't explode!"""
        return "...it's a glove."

    def punch(self):
        """sees how hard the glove can punch!"""
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'

    def fight(self, opp_glove):
        """makes two gloves fight each other!"""
        # I tried to test if opp_glove was a boxing glove, but couldn't
        # get it to work.
        if self.weight > opp_glove.weight:
            return 'This glove wins! The thrill of victory!'
        elif self.weight < opp_glove.weight:
            return 'The other glove wins. The agony of defeat!'
        else:
            return 'The gloves are equally matched. How exciting!'
