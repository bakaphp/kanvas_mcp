# tools/product_tools.py
from fastmcp.tools import tool
from services.inventory.products import search_products as search_products_service


def search_products(name: str) -> str:
    return search_products_service(name)
