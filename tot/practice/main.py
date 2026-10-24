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
                FOREIGN KEY (product_id) REFERENCES     
            )
        """)

init_db()


def add_product_db(name,price,stock):
    if not name or not name.strip():
        return {'success':False,"message":'name cannot be empty!'}
    if price <=0:
        return {'success':False,'message':'price most be higher than 0!'}
    if stock < 0 :
        return {'success':False,'message':'number of product must be gratter than 0 or 0!'}


    try:
        with sqlite3.connect('sales.db') as conn:
            cursor = conn.execute(
                "INSERT INTO products (name,price,stock) VALUES (?,?,?)",(name,price,stock)
            )
            new_id=cursor.lastrowid
            return {'success':True,'message':'product added','product_id':new_id}
    except sqlite3.Error as e:
        return {'success':False,'message':f'database Error {e}'}


def get_product_db():
    try:
        with sqlite3.connect('sales.db') as conn:
            row = conn.execute("SELECT * FROM products").fetchall()
            return row
    finally:
        conn.close()

def get_product_by_id(product_id):
    try:
        with sqlite3.connect('sales.db') as conn:
            row = conn.execute('SELECT * FROM products WHERE id = ?',(product_id,)).fetchone()
            return row
    finally:
        conn.close()



def update_product_stock(product_id: int, new_stock: int) -> dict:
    if new_stock < 0:
        return {
            'success': False,
            'message': 'Stock cannot be negative!'
        }

    conn = sqlite3.connect('sales.db')

    try:
        with conn:
            cursor = conn.execute(
                'UPDATE products SET stock = ? WHERE id = ?',
                (new_stock, product_id)
            )

            if cursor.rowcount == 0:
                return {
                    'success': False,
                    'message': 'Product not found!'
                }

        return {
            'success': True,
            'message': 'Stock updated successfully!'    
        }

    except sqlite3.Error as e:
        return {
            'success': False,
            'message': f'Database error: {e}'
        }

    finally:
        conn.close()



def delete_product(product_id):
    conn = sqlite3.connect('sales.db')

    try:
        with conn:
            cursor = conn.execute('DELETE FROM products WHERE id = ?',(product_id,))
        if cursor.rowcount == 0:
            return{
                'success':False,
                'message':'product dont exist'
            }
        return {
            'success':True,
            'message':'product has been deleted'
        }
    finally:
        conn.close()