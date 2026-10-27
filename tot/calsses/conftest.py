# conftest.py
import pytest
from models import Product

@pytest.fixture
def sample_products():
    """This fixture return a dict of products"""
    return {
        1: Product(id=1, name='Mouse', price=130000, stock=5),
        2: Product(id=2, name='keyboard', price=170000, stock=2)
    }


@pytest.fixture
def single_product():
    """This fixture return a product"""
    return Product(id=1,name='Mouse',price=130000,stock=5)