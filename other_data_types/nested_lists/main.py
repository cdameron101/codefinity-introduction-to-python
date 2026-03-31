vegetables = ["tomatoes", "potatoes", "onions"]
print(vegetables)
vegetables.remove("onions")
print(vegetables)
if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")
    print(vegetables)
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
print("Cucumbers are already in the list.")
print(vegetables)
vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)
