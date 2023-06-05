def problem206_d():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n//2):
        ans += abs(a[i]-a[n-i-1])
    print(ans)
problem206_d()
