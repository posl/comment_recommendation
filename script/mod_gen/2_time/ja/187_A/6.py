def sum_digit(num):
    return sum(map(int, str(num)))
A, B = map(int, input().split())
print(max(sum_digit(A), sum_digit(B)))
