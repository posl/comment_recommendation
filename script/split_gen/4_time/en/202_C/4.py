def p202_c():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    d = [0] * n
    for i in range(n):
        d[c[i]] += 1
    ans = 0
    for i in range(n):
        ans += d[b[a[i] - 1] - 1]
    print(ans)
