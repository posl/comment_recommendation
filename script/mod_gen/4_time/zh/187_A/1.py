def sum_digit(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

if __name__ == '__main__':
    sum_digit()