def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

if __name__ == '__main__':
    sum_digits()