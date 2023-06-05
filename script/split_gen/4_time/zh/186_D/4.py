def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    ans = 0
    for i in range(n):
        ans += a[i] * i - sum(a[:i])
        ans -= a[i] * (n - i - 1) - sum(a[i + 1:])
    print(ans)
