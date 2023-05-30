def sum_digits(num):
    return sum([int(i) for i in str(num)])
A, B = map(int, input().split())
print(max(sum_digits(A), sum_digits(B)))
