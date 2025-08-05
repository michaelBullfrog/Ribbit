import os

def quote_product(sku, quantity):
    # Placeholder logic until API is implemented
    return {
        "sku": sku,
        "quantity": quantity,
        "price": 99.99,
        "total": 99.99 * quantity,
        "description": "Mock description for " + sku
    }

def suggest_replacement(eol_sku):
    # Mock replacement suggestion
    return {
        "original_sku": eol_sku,
        "replacement_sku": eol_sku + "-R",
        "notes": "This is a recommended replacement for the EOL SKU."
    }