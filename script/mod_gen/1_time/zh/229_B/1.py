def plus(a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    result = 0
    carry = 0
    while a > 0 and b > 0:
        if a % 10 + b % 10 + carry >= 10:
            carry = 1
        else:
            carry = 0
        a = a // 10
        b = b // 10
        result = result * 10 + carry
    while a > 0:
        if a % 10 + carry >= 10:
            carry = 1
        else:
            carry = 0
        a = a // 10
        result = result * 10 + carry
    while b > 0:
        if b % 10 + carry >= 10:
            carry = 1
        else:
            carry = 0
        b = b // 10
        result = result * 10 + carry
    return result

if __name__ == '__main__':
    plus()