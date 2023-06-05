def get_max_product(num):
    num_str = str(num)
    max_product = 0
    for i in range(1, len(num_str)):
        num1 = int(num_str[:i])
        num2 = int(num_str[i:])
        product = num1 * num2
        if product > max_product:
            max_product = product
    return max_product

if __name__ == '__main__':
    get_max_product()