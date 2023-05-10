def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)
N = int(input())
print(*s(N))
