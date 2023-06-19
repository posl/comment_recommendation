def sum_digit(num):
    s = str(num)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return sum
a, b = map(int, input().split())
print(max(sum_digit(a), sum_digit(b)))
