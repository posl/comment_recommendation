def sum_digit(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum
A, B = map(int, input().split())
print(max(sum_digit(A), sum_digit(B)))
