# implementing  inventory manager
# from product import Product
from external_service import ExternalService


class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_products(self, product):
        self.inventory[product.name] = product

        ExternalService.add_product_with_logging(product.name)

    def remove_product(self, product_name):
        if product_name in self.inventory:
            del self.inventory[product_name]
        else:
            return 'Product not found'

    def update_quantity(self, product_name, new_quantity):
        if product_name in self.inventory:
            return self.inventory[product_name].update_quantity(new_quantity)
        else:
            return 'Product not found'

    def update_price(self, product_name, new_price):
        if product_name in self.inventory:
            return self.inventory[product_name].update_price(new_price)
        else:
            return 'Product not found'

    def get_product_info(self, product_name):
        if product_name in self.inventory:
            return self.inventory[product_name].get_product_info()
        else:
            return 'Product not found'

    def get_total_inventory_value(self):
        total_value = 0
        for product in self.inventory.values():
            total_value += product.price * product.quantity
        return total_value

    def search_product(self, product_name):
        if product_name in self.inventory:
            product = self.inventory[product_name]
            return product.get_product_info()
        else:
            return 'Product not found in inventory'


'''

inventory_manager = InventoryManager()

p1 = Product('laptop', 1000, 100)
p2 = Product('Mouse', 250, 100)
p3 = Product('keyboard', 200, 100)

inventory_manager.add_products(p1)
inventory_manager.add_products(p2)
inventory_manager.add_products(p3)


print(inventory_manager.get_product_info('laptop'))
inventory_manager.update_price('laptop', 200)
inventory_manager.update_quantity('laptop', 30)
print(inventory_manager.get_product_info('Mouse'))
print(inventory_manager.get_product_info('keyboard'))
print(inventory_manager.get_total_inventory_value())


print(inventory_manager.search_product('Mouse'))
'''
