def sum_of_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
n = int(input())
print('Yes' if n % sum_of_digit(n) == 0 else 'No')
