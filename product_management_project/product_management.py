# ecommerce/products/product_management.py

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def update_price(self, new_price):
        self.price = new_price

    def __str__(self):
        return f"Product(id={self.product_id}, name={self.name}, price={self.price}, stock={self.stock})"

def add_product(products, product):
    products.append(product)

def remove_product(products, product_id):
    products[:] = [product for product in products if product.product_id != product_id]
