def sum_digits(num):
    sum = 0
    while num:
        sum += num % 10
        num //= 10
    return sum

if __name__ == '__main__':
    sum_digits()