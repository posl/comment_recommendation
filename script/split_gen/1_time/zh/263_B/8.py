def problem263_b():
    n = int(input())
    p = [0] + list(map(int, input().split()))
    d = [0] * (n + 1)
    for i in range(n, 0, -1):
        d[i] = d[p[i]] + 1
    print(max(d))
