def power(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

if __name__ == '__main__':
    power()