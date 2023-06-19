def s(n):
    if n == 1:
        return [1]
    else:
        sn = s(n-1)
        return sn + [n] + sn
n = int(input())
print(*s(n))
