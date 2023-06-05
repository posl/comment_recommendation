def S(n):
    return sum([int(i) for i in str(n)])
a, b = [int(i) for i in input().split()]
print(S(a) if S(a) > S(b) else S(b))
