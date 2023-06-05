def get_cost(a, b):
    if a >= 13:
        return b
    elif a >= 6:
        return b // 2
    else:
        return 0

if __name__ == '__main__':
    get_cost()