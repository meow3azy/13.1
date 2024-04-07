import pytest
from main import Category, Product

@pytest.fixture
def create_category():
    Category.total_categories = 0
    return Category("Название категории", "Описание категории")
@pytest.fixture
def create_product():
    return Product("Название продукта", "Описание продукта", 100, 10)

def test_category_initialization(create_category):
    category = create_category
    assert category.name == "Название категории"
    assert category.description == "Описание категории"

def test_product_initialization(create_product):
    product = create_product
    assert product.name == "Название продукта"
    assert product.description == "Описание продукта"
    assert product.price == 100
    assert product.quantity == 10

def test_count_products(create_category, create_product):
    category = create_category
    product = create_product
    category.add_product(product)
    assert len(category.products) == 1

def test_count_categories(create_category):
    category = create_category
    assert Category.total_categories == 1

