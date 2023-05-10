def compute_product_of_list(list):
    product = 1
    for item in list:
        product *= item
        if product > 10**18:
            return -1
    return product
