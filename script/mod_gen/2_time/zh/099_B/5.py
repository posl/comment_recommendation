def snow(a, b):
    total = 0
    for i in range(1, a):
        total += i
    for i in range(b+1):
        total += i
    return total - a - b

if __name__ == '__main__':
    snow()