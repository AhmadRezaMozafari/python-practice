from fastapi import FastAPI, HTTPException, Depends
import sqlite3

from models import Product
from repository import get_all_products, save_product, update_product_stock, delete_product
from schemas import ProductCreate, ProductResponse, StockUpdate
from main import init_db  # از فایل main برای ساخت جدول استفاده میکنیم

app = FastAPI(title="Store API", description="سیستم مدیریت محصولات")

# این تابع به FastAPI میگه برای هر درخواست، یک اتصال به دیتابیس باز کن و بعد ببند
def get_db():
    conn = sqlite3.connect("store.db")
    init_db(conn) # مطمئن میشیم جدول وجود داره
    try:
        yield conn
    finally:
        conn.close()

# ==================== Endpoints ====================

# ۱. دریافت لیست همه محصولات (GET)
@app.get("/products", response_model=list[ProductResponse])
def read_products(db: sqlite3.Connection = Depends(get_db)):
    return get_all_products(db)

# ۲. اضافه کردن محصول جدید (POST)
@app.post("/products", response_model=ProductResponse, status_code=201)
def create_product(product_in: ProductCreate, db: sqlite3.Connection = Depends(get_db)):
    new_product = Product(id=0, name=product_in.name, price=product_in.price, stock=product_in.stock)
    saved_product = save_product(db, new_product)
    return saved_product

# ۳. تغییر موجودی (PUT)
@app.put("/products/{product_id}/stock")
def update_stock(product_id: int, stock_data: StockUpdate, db: sqlite3.Connection = Depends(get_db)):
    success = update_product_stock(db, product_id, stock_data.new_stock)
    if not success:
        raise HTTPException(status_code=404, detail="محصول پیدا نشد")
    return {"message": "موجودی با موفقیت آپدیت شد"}

# ۴. حذف محصول (DELETE)
@app.delete("/products/{product_id}")
def remove_product(product_id: int, db: sqlite3.Connection = Depends(get_db)):
    success = delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="محصول پیدا نشد")
    return {"message": "محصول با موفقیت حذف شد"}