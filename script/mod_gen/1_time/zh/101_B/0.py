def sum_digit(n):
    sum = 0
    while n > 0:
        sum += n%10
        n = n//10
    return sum

if __name__ == '__main__':
    sum_digit()