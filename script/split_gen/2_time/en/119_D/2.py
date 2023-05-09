def main():
    A, B, Q = map(int, input().split())
    s = [-10**10] + [int(input()) for _ in range(A)] + [10**10]
    t = [-10**10] + [int(input()) for _ in range(B)] + [10**10]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        s_idx = bisect_left(s, x[i])
        t_idx = bisect_left(t, x[i])
        ans = 10**20
        for s_i in [s[s_idx-1], s[s_idx]]:
            for t_i in [t[t_idx-1], t[t_idx]]:
                ans = min(ans, max(s_i, t_i) - x[i])
                ans = min(ans, x[i] - min(s_i, t_i))
        print(ans)
