def S(n):
    if n == 1:
        return [1]
    else:
        a = S(n-1)
        return a + [n] + a
n = int(input())
print(*S(n))
