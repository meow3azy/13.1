class Category:
    total_categories = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.total_unique_products = len(set(product.name for product in products))
        Category.total_categories += 1

    def add_product(self, product):
        self.products.append(product)
        self.total_unique_products = len(set(product.name for product in self.products))



class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
