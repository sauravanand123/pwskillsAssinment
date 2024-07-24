# ecommerce/orders/order_processing.py

class Order:
    def __init__(self, order_id, customer_name, products):
        self.order_id = order_id
        self.customer_name = customer_name
        self.products = products
        self.status = "Pending"

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [product for product in self.products if product.product_id != product_id]

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        products_list = ', '.join([str(product) for product in self.products])
        return f"Order(id={self.order_id}, customer={self.customer_name}, products=[{products_list}], status={self.status})"

def process_order(order):
    order.update_status("Processed")
