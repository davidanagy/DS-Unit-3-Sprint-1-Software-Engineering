import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_methods(self):
        """Test methods work properly."""
        prod = Product('Test Product', price=1, weight=10, flammability=10)
        self.assertEqual('Not so stealable...', prod.stealability())
        self.assertEqual('...BABOOM!!', prod.explode())


legal_names = []
for adj in ADJECTIVES:
    for noun in NOUNS:
        legal_names.append(adj + ' ' + noun)


class AcmeReportTests(unittest.TestCase):
    """Making sure our reports are true and good!"""
    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = generate_products()
        for prod in products:
            self.assertIn(prod.name, legal_names)


if __name__ == '__main__':
    unittest.main()
