def perm2num(p):
    n = len(p)
    a = [0] * n
    for i in range(n):
        a[i] = p[i]
        for j in range(i):
            if a[j] > a[i]:
                a[j] -= 1
    num = 0
    for i in range(n):
        num += a[i] * math.factorial(n - 1 - i)
    return num

if __name__ == '__main__':
    perm2num()