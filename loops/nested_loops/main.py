produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

# Combine into one list
groceries = [produce, dairy]

# Nested loops to print each item
for section in groceries:
    for item in section:
        print("Item name:", item)