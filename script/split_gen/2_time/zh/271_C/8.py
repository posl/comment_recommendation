def problem271_c():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = 0
    for i in range(n):
        if a[i] >= i + 1:
            ans += 1
    print(ans)
