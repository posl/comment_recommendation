def problems113_b():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min_diff = 100000
    for i in range(n):
        temp = t - h[i] * 0.006
        if abs(a - temp) < min_diff:
            min_diff = abs(a - temp)
            ans = i + 1
    print(ans)
