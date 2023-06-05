def S(n):
    if n == 1:
        return [1]
    else:
        s = S(n-1)
        return s + [n] + s
n = int(input())
print(*S(n))
