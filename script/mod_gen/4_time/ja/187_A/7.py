def sum_digits(number):
    return sum([int(digit) for digit in str(number)])
a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

if __name__ == '__main__':
    sum_digits()