import sqlite3
from models import Product


def save_product(conn:sqlite3.Connection,product:Product) -> Product:
    cursor=conn.execute("""
        INSERT INTO products (name,price,stock) VALUES (?,?,?)
    """,(product.name,product.price,product.stock)
    )
    conn.commit()
    product.id=cursor.lastrowid

    return product


def get_all_products(conn:sqlite3.Connection) -> list[Product]:
    cursor = conn.execute('SELECT id,name,price,stock FROM products')

    rows = cursor.fetchall()

    products=[]

    for row in rows:
        p = Product(
            id=row[0],
            name=row[1],
            price=row[2],
            stock=row[3]
        )

        products.append(p)
    return products


def update_product_stock(conn:sqlite3.Connection,product_id:int,new_stock:int) -> bool:
    cursor = conn.execute("UPDATE products SET stock = ? WHERE id = ?",(new_stock,product_id))

    conn.commit()

    return cursor.rowcount > 0


def delete_product(conn:sqlite3.Connection,product_id:int)->bool:
    cursor = conn.execute(
        "DELETE FROM products WHERE id = ?",(product_id,)
    )
    conn.commit()

    return cursor.rowcount > 0