def get_max_num_of_coins(a, b):
    if a == b:
        return a + b
    else:
        return max(a, b) + max(a, b) - 1

if __name__ == '__main__':
    get_max_num_of_coins()