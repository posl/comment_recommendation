def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += a[i]
    if a[n-1] > ans + 1:
        ans = 0
    else:
        ans += a[n-1]
    print(ans)
