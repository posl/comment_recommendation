def f(m):
    res = 0
    for i in range(n):
        res += m % a[i]
    return res
n = int(input())
a = list(map(int, input().split()))
a.sort()
print(f(a[-1] - 1))
