def s(n):
    return sum(map(int, str(n)))
a, b = map(int, input().split())
print(s(a) if s(a) > s(b) else s(b))
