def problem202c():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = [0] * (n + 1)
    for i in range(n):
        d[b[c[i] - 1]] += 1
    ans = 0
    for i in range(n):
        ans += d[a[i]]
    print(ans)
