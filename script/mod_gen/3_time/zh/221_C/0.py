def get_max_product(num_str):
    if len(num_str) == 2:
        return int(num_str[0]) * int(num_str[1])
    max_product = 0
    for i in range(1, len(num_str)):
        left = num_str[:i]
        right = num_str[i:]
        if left[0] == '0' or right[0] == '0':
            continue
        product = int(left) * int(right)
        if product > max_product:
            max_product = product
    return max_product

if __name__ == '__main__':
    get_max_product()