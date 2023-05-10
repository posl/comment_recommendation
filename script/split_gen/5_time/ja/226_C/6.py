def get_input():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [0] * n
    for i in range(n):
        t[i], k[i] = map(int, input().split())
        a[i] = list(map(int, input().split()))
    return n, t, k, a
