def sum_of_digits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n /= 10
    return sum
a, b = map(int, raw_input().split())
print max(sum_of_digits(a), sum_of_digits(b))
