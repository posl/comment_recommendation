def S(n):
    return sum([int(i) for i in str(n)])
a, b = map(int, input().split())
print(max(S(a), S(b)))
