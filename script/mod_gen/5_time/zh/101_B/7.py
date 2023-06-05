def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

if __name__ == '__main__':
    sum_digits()