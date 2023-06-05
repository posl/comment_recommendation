def f(a, b):
    if a == b:
        return a
    elif a + 1 == b:
        return a ^ b
    elif a % 2 == 0 and b % 2 == 0:
        return f(a, b - 1) ^ b
    elif a % 2 == 0 and b % 2 == 1:
        return f(a, b - 1)
    elif a % 2 == 1 and b % 2 == 0:
        return f(a, b) ^ b
    else:
        return f(a, b) ^ b

if __name__ == '__main__':
    f()