def get_num(num):
    a = num // 100
    b = num // 10 % 10
    c = num % 10
    return a, b, c
