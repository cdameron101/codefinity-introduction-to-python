def apply_discount(price, discount=0.05):
    return price * (1 - discount)

def apply_tax(price, tax=0.07):
    return price * (1 + tax)

def calculate_total(price, discount=0.05, tax=0.07):
    discounted = apply_discount(price, discount)
    total = apply_tax(discounted, tax)
    return total

# Default case
total = calculate_total(120)
print(f"Total cost with default discount and tax: ${total:.2f}")

# Custom case
custom_total = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${custom_total:.2f}")
# Use correct price and formatting
total = calculate_total(120)

print(f"Total cost with default discount and tax: ${total:.2f}")