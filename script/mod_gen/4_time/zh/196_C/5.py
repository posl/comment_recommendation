def f(n):
    if n < 11:
        return 0
    if n < 101:
        return (n - 10) // 11 + 1
    if n < 1001:
        return 9 + (n - 100) // 111 + 1
    if n < 10001:
        return 9 + 90 + (n - 1000) // 1111 + 1
    if n < 100001:
        return 9 + 90 + 900 + (n - 10000) // 11111 + 1
    if n < 1000001:
        return 9 + 90 + 900 + 9000 + (n - 100000) // 111111 + 1
    if n < 10000001:
        return 9 + 90 + 900 + 9000 + 90000 + (n - 1000000) // 1111111 + 1
    if n < 100000001:
        return 9 + 90 + 900 + 9000 + 90000 + 900000 + (n - 10000000) // 11111111 + 1
    if n < 1000000001:
        return 9 + 90 + 900 + 9000 + 90000 + 900000 + 9000000 + (n - 100000000) // 111111111 + 1
    if n < 10000000001:
        return 9 + 90 + 900 + 9000 + 90000 + 900000 + 9000000 + 90000000 + (n - 1000000000) // 1111111111 + 1
    if n < 100000000001:
        return 9 + 90 + 900 + 9000 + 90000 + 900000 + 9000000 + 90000000 + 900000000 + (n - 10000000000) // 11111111111 + 1
    if n < 1000000000001:
        return 9 + 90 + 900 + 9000 + 90000 + 900000 + 9000000 + 90000000 + 900000000 + 9000000000 +

if __name__ == '__main__':
    f()