import pytest

from main import *
from repository import *

@pytest.mark.parametrize('price,stock,expected_in_stock, expected_total_value',[
    (130000, 5, True, 650000),
    (200000, 0, False, 0),
    (50000, 1, True, 50000),
],ids=['in stock','out of stock','one item left'])
def test_product_properties(price, stock, expected_in_stock, expected_total_value):
    p = Product(id=1, name="TestProduct", price=price, stock=stock)
    
    assert p.is_in_stock() is expected_in_stock
    assert p.total_value() == expected_total_value


@pytest.mark.parametrize("price, quantity, expected_total", [
    (130000, 2, 260000),          
    (150000, 3, 450000),
    (100000, 0, 0),
], ids=["two_items", "three_items", "zero_quantity"])
def test_order_calculate_total(price, quantity, expected_total):
    p = Product(id=1, name="TestProduct", price=price, stock=10)
    
    o = Order(id=1, customer="ali", product=p, quantity=quantity, unit_price=price)
    
    assert o.calculate_total() == expected_total


@pytest.mark.parametrize("product_id, quantity, expected_message", [
    (1, 3, "purchase completed"), 
    (2, 5, "not enough stock!"),  
    (99, 1, "product doesn't exist!"),
])
def test_register_order_scenarios(sample_products, product_id, quantity, expected_message):
    orders = []
    
    result = register_order(
        products=sample_products,
        orders=orders,
        customer='ali',
        product_id=product_id,
        quantity=quantity
    )
    
    assert expected_message in result

def test_save_product_to_db(db_connection):
    product = Product(id=0,name='Monitor',price=500000,stock=5)

    saved_product = save_product(db_connection,product=product)

    assert saved_product.id == 1

    row = db_connection.execute("SELECT name,price,stock FROM products WHERE id = 1").fetchone()

    assert row[0] == "Monitor"
    assert row[1] == 500000
    assert row[2] == 5


def test_get_all_products(db_connection):
    p1 = Product(id=0, name="Mouse", price=500000, stock=10)
    p2 = Product(id=0, name="Keyboard", price=1500000, stock=5)
    save_product(db_connection, p1)
    save_product(db_connection, p2)

    all_products = get_all_products(db_connection)
    assert len(all_products) == 2
    assert all_products[0].name == "Mouse"
    assert all_products[1].name == "Keyboard"


def test_update_product_stock(db_connection):
    p = Product(id=0,name='Monitor',price=400000,stock=6)

    save_product(db_connection,p)

    result = update_product_stock(db_connection,product_id=p.id,new_stock=10)

    assert result == True
# def test_product_in_stock(single_product):
#     p = single_product

#     assert p.is_in_stock() is True
#     assert p.total_value() == 650000


# def test_product_out_of_stock(single_product):
#     p = single_product

#     assert p.is_in_stock() is False
#     assert p.total_value() == 0


# def test_order_calculate_total(single_product):
#     p = single_product

#     o=Order(id=1,customer='ali',product=p,quantity=2,unit_price=p.price)

#     assert o.calculate_total() == 260000

# def test_register_order(sample_products):
#     orders=[]

#     result = register_order(products=sample_products,orders=orders,customer='ali',product_id=1,quantity=3)

#     assert 'purchase completed' in result
#     assert len(orders) == 1
#     assert sample_products[1].stock == 2

# def test_register_order_not_enough_stock(sample_products):
#     orders=[]
#     result = register_order(products=sample_products,orders=orders,customer='ali',product_id=2,quantity=3)

#     assert "not enough stock!" in result
#     assert sample_products[2].stock == 2
#     assert len(orders) == 0

# def test_register_order_product_not_found(sample_products):

#     orders=[]
#     result = register_order(products=sample_products,orders=orders,customer='ali',product_id=99,quantity=3)

#     assert "product doesn't exist!" in result

    