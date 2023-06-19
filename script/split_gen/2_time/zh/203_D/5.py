def get_median(a):
    a.sort()
    n = len(a)
    if n % 2 == 0:
        return a[n // 2 - 1]
    else:
        return a[n // 2]
n, k = map(int, input().split())
a = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
ans = 10 ** 9 + 1
for i in range(n - k + 1):
    for j in range(n - k + 1):
        b = []
        for p in range(k):
            for q in range(k):
                b.append(a[i + p][j + q])
        ans = min(ans, get_median(b))
print(ans)
