import unittest
from unittest.mock import patch
from product import Product
from inventory_manager import InventoryManager

# creating a class for testing


class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.inventory_manager = InventoryManager()
        self.p1 = Product('Laptop', 1200, 10)
        self.p2 = Product('Mouse', 250, 10)
        self.p3 = Product('Keyboard', 450, 10)

        self.inventory_manager.add_products(self.p1)
        self.inventory_manager.add_products(self.p2)
        self.inventory_manager.add_products(self.p3)

    def test_add_products(self):
        self.assertIn('Laptop', self.inventory_manager.inventory)
        self.assertIn('Mouse', self.inventory_manager.inventory)
        self.assertIn('Keyboard', self.inventory_manager.inventory)

    def test_remove_product(self):
        self.inventory_manager.remove_product('Mouse')
        self.assertNotIn('Mouse', self.inventory_manager.inventory)

    def test_update_quantity(self):
        self.inventory_manager.update_quantity('Laptop', 20)
        self.assertEqual(self.inventory_manager.inventory['Laptop'].quantity, 20) # noqa

    def test_update_price(self):
        self.inventory_manager.update_quantity('Laptop', 1200)
        self.assertEqual(self.inventory_manager.inventory['Laptop'].price, 1200) # noqa

    def test_get_product_info(self):
        info = 'Product: Laptop, Price: € 1200.00, Quantity: 10'
        self.assertEqual(self.inventory_manager.get_product_info('Laptop'), info) # noqa

    def test_get_total_inventory_valuse(self):
        total_value = 19000
        self.assertEqual(self.inventory_manager.get_total_inventory_value(), total_value) # noqa

    @patch('external_service.ExternalService.add_product_with_logging')
    def test_add_product_with_logging(self, mock_logging):
        new_product = Product('Tablet', 10, 350)
        self.inventory_manager.add_products(new_product)
        mock_logging.assert_called_once_with('Tablet')


if __name__ == '__main__':
    unittest.main()
