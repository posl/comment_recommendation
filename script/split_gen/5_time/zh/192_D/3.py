def f(x, m):
    d = 0
    for i in x:
        d = max(d, int(i))
    l = d + 1
    r = m + 1
    while r - l > 1:
        mid = (l + r) // 2
        t = 0
        k = 1
        for i in range(len(x) - 1, -1, -1):
            t += k * int(x[i])
            k *= mid
        if t <= m:
            l = mid
        else:
            r = mid
    return l - d
x = input()
m = int(input())
print(f(x, m))
