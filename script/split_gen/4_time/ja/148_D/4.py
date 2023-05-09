def problems148_d():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        if a[i] == ans + 1:
            ans += 1
    if ans == 0:
        print(-1)
    else:
        print(n - ans)
