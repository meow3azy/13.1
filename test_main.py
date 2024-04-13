import pytest
from main import Category, Product

def existing_category():
    return Category("Существующая категория", "Описание существующей категории", [])

def test_count_categories(existing_category):
    assert Category.total_categories == 1

@pytest.fixture
def create_category():
    return Category("Название категории", "Описание категории", [])

@pytest.fixture
def create_product():
    return Product("Название продукта", "Описание продукта", 100, 10)

def test_category_initialization(create_category):
    category = create_category
    assert category.name == "Название категории"
    assert category.description == "Описание категории"
    assert category.products == []

def test_product_initialization(create_product):
    product = create_product
    assert product.name == "Название продукта"
    assert product.description == "Описание продукта"
    assert product.price == 100
    assert product.quantity == 10

def test_add_product_to_category(create_category, create_product):
    category = create_category
    product = create_product
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == product

def test_count_categories(create_category):
    assert Category.total_categories == 1

def test_count_unique_products(create_category, create_product):
    category = create_category
    product = create_product
    category.add_product(product)
    assert category.total_unique_products == 1

def test_count_products(create_category, create_product):
    category = create_category
    product = create_product
    category.add_product(product)
    assert len(category.products) == 1
