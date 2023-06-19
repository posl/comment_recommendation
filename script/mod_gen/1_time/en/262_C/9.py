def f(a):
    n = len(a)
    s = [0] * (n + 2)
    for i in range(n):
        s[a[i]] = i + 1
    s[n + 1] = 10**6
    res = 0
    for i in range(1, n + 1):
        if s[i] == i:
            x = s[i + 1]
            while x < n + 1 and s[x] == x:
                x += 1
            res += x - i
    return res
n = int(input())
a = [int(x) for x in input().split()]
print(f(a))
