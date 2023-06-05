def sum_digit(num):
    res = 0
    while num > 0:
        res += num % 10
        num //= 10
    return res

if __name__ == '__main__':
    sum_digit()