from product import Product
from inventory_manager import InventoryManager
# from external_service import ExternalService

inventory_manager = InventoryManager()


while True:
    print("\n******Welcome To Inventory Management System******")
    print("\nSelect Your Choices And Enter Below.")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Quantity")
    print("4. Update Price")
    print("5. Get Product Info")
    print("6. List All Products")
    print("7. Get Total Inventory Value")
    print("8. Search Products")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input('Enter Product Name: ').lower()
        quantity = int(input('Enter the Quantity: '))
        price = float(input('Enter the Price: '))
        product = Product(name, price, quantity)
        inventory_manager.add_products(product)
        print(f"Product: {product.name} added to the inventory.")

    elif choice == '2':
        name = input('Enter Product name to remove: ')
        result = inventory_manager.remove_product(name)
        if result == 'Product not found':
            print(result)
        else:
            print(f'Product: {name} removed from the inventory')

    elif choice == '3':
        name = input('Enter Product name to update quantity: ')
        new_quantity = int(input('Enter new quantity:'))
        result = inventory_manager.update_quantity(name, new_quantity)
        if result == 'If Product does not Exists':
            print(result)
        else:
            print(f'Product: {name} quantity updated to {new_quantity}.')

    elif choice == '4':
        name = input('Enter Product name to update price: ')
        new_price = int(input('Enter new Price :'))
        result = inventory_manager.update_price(name, new_price)
        if result == 'If Product does not Exists':
            print(result)
        else:
            print(f'Product: {name} price updated to {new_price}.')

    elif choice == '5':
        name = input('Enter Product Name to get  Information: ')
        print(inventory_manager.get_product_info(name))

    elif choice == '6':
        print('\n __________INVENTORY DETAILS_________')
        for product in inventory_manager.inventory.values():
            print(f'Product Name: {product.name}')
            print(f'Product Price: € {product.price}')
            print(f'Quantity: {product.quantity}')
            print('____________________________________')

    elif choice == '7':
        print(f'Total inventory value: € {inventory_manager.get_total_inventory_value()}') # noqa

    elif choice == '8':
        name = input('Enter the product name to search: ')
        if name in inventory_manager.inventory:
            product = inventory_manager.inventory[name]
            print(f'{product.get_product_info()}')
        else:
            print('Product not found')

    elif choice == '9':
        print('Thnak you for visiting, you are now exited from the Inventory management system') # noqa
        break
    else:
        print('Invalid Choice')
