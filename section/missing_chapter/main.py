item1 = 162 * 1.2
item2 = 25 - 3

subtotal = item1 + item2
tax = subtotal * 0.08

print("Shopping Receipt")
print("-----------------------")            # 1st divider
print(f"Item 1: ${item1}")
print(f"Item 2: ${item2}")
print("-----------------------")            # 2nd divider
print(f"Subtotal: ${subtotal}")
print(f"Tax (8%): ${tax}")
print("-----------------------")            # optional divider before footer
print("Thank you for shopping!")
