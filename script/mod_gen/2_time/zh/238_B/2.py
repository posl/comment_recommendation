def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(a[0] + 360)
    ans = 0
    for i in range(n):
        ans = max(ans, a[i + 1] - a[i])
    print(360 - ans)
    return 0
func()
