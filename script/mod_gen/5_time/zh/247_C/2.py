def sn(n):
    if n == 1:
        return [1]
    else:
        return sn(n-1) + [n] + sn(n-1)
n = int(input())
print(*sn(n))
