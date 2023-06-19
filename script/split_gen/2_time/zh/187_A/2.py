def s(n):
    sum = 0
    for i in range(3):
        sum += n % 10
        n //= 10
    return sum
a, b = map(int, input().split())
print(s(a) if s(a) > s(b) else s(b))
