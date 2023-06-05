def resolve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i] * (i + 1)
    ans = sum
    for i in range(m):
        sum -= a[n - 1 - i] * (n - i)
        sum += a[i] * (n - i)
        ans = max(ans, sum)
    print(ans)
