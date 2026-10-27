from models import Order,Product


def register_order(products:dict[int, Product],orders:list[Order],customer:str,product_id:int,quantity:int):
    if product_id not in products:
        return "product doesn't exist!"

    product=products[product_id]

    if not product.is_in_stock():
        return "this product is out of sale"

    if product.stock < quantity:
        return "not enough stock!"

    order_id = len(orders)+1

    new_order = Order (id=order_id,customer=customer,product=product,quantity=quantity,unit_price=product.price)

    product.stock -= quantity
    orders.append(new_order)

    return f"purchase completed,\ntotal: {new_order.calculate_total()}"



def calculate_customer_purchases(orders:list[dict], customer:str)->int:
    total = 0
    for order in orders:
        if order.customer == customer:
            total+=order.calculate_total()

    return total            



if __name__ == "__main__":
   p1 = Product(id=1, name="Keyboard", price=1500000, stock=5)
   p2 = Product(id=2, name="Mouse", price=800000, stock=10)
   my_orders = [
        Order(id=1, customer="Ali", product=p1, quantity=2),  
        Order(id=2, customer="Sara", product=p2, quantity=1),  
        Order(id=3, customer="Ali", product=p2, quantity=3),   
    ]
   ali_total = calculate_customer_purchases(my_orders, "Ali")
   print(f"ali total: {ali_total}")