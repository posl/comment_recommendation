def get_max(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return max(add, sub, mul)

if __name__ == '__main__':
    get_max()