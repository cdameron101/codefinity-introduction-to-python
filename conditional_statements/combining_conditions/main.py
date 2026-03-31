discounted = False
lowStock = True

# True if item is discounted OR low in stock
movingProduct = discounted or lowStock

# True if NOT discounted AND NOT low in stock
promotion = not discounted and not lowStock

print("Is the item eligible for promotion?", promotion)