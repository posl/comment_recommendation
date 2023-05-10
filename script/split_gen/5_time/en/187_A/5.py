def sum_digits(number):
    return sum(int(digit) for digit in str(number))
a, b = map(int, input().split())
