def problems221_d():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    ans = [0] * (n + 1)
    for i in range(n):
        ans[a[i]] += 1
        ans[a[i] + b[i]] -= 1
    for i in range(1, n + 1):
        ans[i] += ans[i - 1]
    ans.pop(0)
    print(*ans)
    return
problems221_d()
