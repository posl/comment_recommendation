def solve():
    n = int(input())
    a = list(map(int,input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = i
    a.sort()
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[n-1] = n-1
        elif a[i] != a[i-1]:
            ans[n-1] += n-i-1
    for i in range(n-2,-1,-1):
        ans[i] = ans[i+1] - n + d[a[i]] + 1
    for i in range(n):
        print(ans[i])
