import sqlite3
def init_db():
    with sqlite3.connect("sales.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price INTEGER NOT NULL CHECK(price > 0),
                stock INTEGER NOT NULL CHECK(stock >= 0)
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer TEXT NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL CHECK(quantity > 0),
                total INTEGER NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        """)

init_db()

def register_order_db(customer: str, product_id: int, quantity: int) -> dict:
    if not customer or not customer.strip():
        return {
            'success':False,
            'message':'customer is empty'
        }
    if quantity < 1 :
        return {
        'success':False,
        'message':'number of order must be gratter than 0!'
    }
    
    conn = sqlite3.connect('sales.db')
    try:
        with conn:
            cursor = conn.execute('SELECT price,stock FROM products WHERE id = ?',(product_id,)).fetchone()

            if cursor is None:
                return {
                    'success':False,
                    'message':'product dosent exist!'
                }
            price,stock=cursor
        
            if stock < 1 :
                return {
                    'success':False,
                    'message':'product stock is 0'
                }
            if stock < quantity:
                return {
                    'success':False,
                    'message':'quantity is more than our stock'
                }

            total_price = price * quantity
            update_order=conn.execute(
                "UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?",(quantity,product_id,quantity,)
            )
            if update_order.rowcount == 0:
                return {
                    'success':False,
                    "message":'stock not enogh'
                }
            order_cursor=conn.execute(
                'INSERT INTO orders (customer,product_id,quantity,total) VALUES (?,?,?,?)',
                (customer,product_id,quantity,total_price,)
                )
            order_id=order_cursor.lastrowid
        return {
        'success': True,
        'message': 'Order registered successfully',
        'total': total_price
}
    finally:
        conn.close()

result = register_order_db("Ali", 12, 2)
print(result)



# import sqlite3

# DB_PATH = "sales.db"

# def get_connection():
#     return sqlite3.connect(DB_PATH)

# def init_db():
#     with get_connection() as conn:
#         conn.execute("""
#             CREATE TABLE IF NOT EXISTS products (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 price INTEGER NOT NULL CHECK(price > 0),
#                 stock INTEGER NOT NULL CHECK(stock >= 0)
#             )
#         """)
#         conn.execute("""
#             CREATE TABLE IF NOT EXISTS orders (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 customer TEXT NOT NULL,
#                 product_id INTEGER NOT NULL,
#                 quantity INTEGER NOT NULL CHECK(quantity > 0),
#                 total INTEGER NOT NULL,
#                 FOREIGN KEY (product_id) REFERENCES products(id)
#             )
#         """)

# def add_product(name: str, price: int, stock: int) -> int:
#     with get_connection() as conn:
#         cursor = conn.execute(
#             "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
#             (name, price, stock)
#         )
#         return cursor.lastrowid

# def register_order_db(customer: str, product_id: int, quantity: int) -> dict:
#     if not customer or not customer.strip():
#         return {'success': False, 'message': 'customer is empty'}

#     if quantity < 1:
#         return {'success': False, 'message': 'quantity must be greater than 0'}

#     conn = get_connection()
#     try:
#         with conn:
#             row = conn.execute(
#                 "SELECT price, stock FROM products WHERE id = ?",
#                 (product_id,)
#             ).fetchone()

#             if row is None:
#                 return {'success': False, 'message': 'product does not exist'}

#             price, stock = row

#             if stock < quantity:
#                 return {
#                     'success': False,
#                     'message': f'not enough stock (available: {stock})'
#                 }

#             total_price = price * quantity

#             updated = conn.execute(
#                 "UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?",
#                 (quantity, product_id, quantity)
#             )

#             if updated.rowcount == 0:
#                 return {'success': False, 'message': 'not enough stock (race condition)'}

#             order_cursor = conn.execute(
#                 "INSERT INTO orders (customer, product_id, quantity, total) VALUES (?, ?, ?, ?)",
#                 (customer, product_id, quantity, total_price)
#             )

#             return {
#                 'success': True,
#                 'message': 'Order registered successfully',
#                 'order_id': order_cursor.lastrowid,
#                 'total': total_price
#             }
#     finally:
#         conn.close()

# if __name__ == "__main__":
#     init_db()
#     pid = add_product("Keyboard", 1500000, 5)
#     result = register_order_db("Ali", pid, 2)
#     print(result)