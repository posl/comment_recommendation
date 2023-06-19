def S(n):
    if n == 1:
        return [1]
    else:
        return S(n-1) + [n] + S(n-1)
n = int(input())
print(' '.join(map(str, S(n))))
