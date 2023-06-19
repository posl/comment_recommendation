def solve():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min_d = 10**6
    min_i = 0
    for i in range(n):
        d = abs(a - (t - h[i] * 0.006))
        if d < min_d:
            min_d = d
            min_i = i + 1
    print(min_i)
