def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices
product_list = ["Apple", "Banana", "Orange", "Apple", "Grapes"]
target = "Apple"
result = linear_search_product(product_list, target)
if result:
    print(f"{target} found at indices: {result}")
else:
    print(f"{target} not found in the list.")
