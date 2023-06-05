def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += a[i]
    if a[n-1] <= ans*2:
        ans += a[n-1]
    else:
        ans = a[n-1]//2
    print(ans)
