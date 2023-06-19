def s(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum
a, b = map(int, input().split())
print(s(a) if s(a) > s(b) else s(b))
