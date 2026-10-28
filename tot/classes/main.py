import sqlite3
from models import Product, Order
from repository import save_product, get_all_products, update_product_stock, delete_product

def init_db(conn: sqlite3.Connection):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            stock INTEGER NOT NULL
        )
    """)
    conn.commit()


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

def main():
    # ۱. اتصال به دیتابیس اصلی
    conn = sqlite3.connect("store.db")
    init_db(conn)

    while True:
        print("\n" + "="*30)
        print("  سیستم مدیریت انبار")
        print("="*30)
        print("1. افزودن محصول جدید")
        print("2. نمایش لیست محصولات")
        print("3. تغییر موجودی")
        print("4. حذف محصول")
        print("5. خروج")
        
        choice = input("\nیک گزینه را انتخاب کنید (1-5): ")

        if choice == "1":
            name = input("نام محصول: ")
            price = int(input("قیمت: "))
            stock = int(input("موجودی اولیه: "))
            
            new_p = Product(id=0, name=name, price=price, stock=stock)
            saved_p = save_product(conn, new_p)
            print(f"✅ محصول '{saved_p.name}' با شناسه {saved_p.id} ذخیره شد.")

        elif choice == "2":
            products = get_all_products(conn)
            if not products:
                print("❌ هیچ محصولی در انبار نیست.")
            else:
                print("\n--- لیست محصولات ---")
                for p in products:
                    print(f"ID: {p.id} | نام: {p.name} | قیمت: {p.price} | موجودی: {p.stock}")

        elif choice == "3":
            p_id = int(input("شناسه محصولی که می‌خواهید تغییر دهید: "))
            new_stock = int(input("موجودی جدید: "))
            
            success = update_product_stock(conn, p_id, new_stock)
            if success:
                print("✅ موجودی با موفقیت به‌روزرسانی شد.")
            else:
                print("❌ محصولی با این شناسه پیدا نشد.")

        elif choice == "4":
            p_id = int(input("شناسه محصولی که می‌خواهید حذف کنید: "))
            
            success = delete_product(conn, p_id)
            if success:
                print("✅ محصول حذف شد.")
            else:
                print("❌ محصولی با این شناسه پیدا نشد.")

        elif choice == "5":
            print("خداحافظ! 👋")
            break  # از حلقه خارج میشه
        
        else:
            print("❌ گزینه نامعتبر است. لطفاً عددی بین ۱ تا ۵ وارد کنید.")

    conn.close()

if __name__ == "__main__":
    main()