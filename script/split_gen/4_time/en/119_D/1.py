def main():
    A, B, Q = map(int, input().split())
    s = [-10**20] + [int(input()) for _ in range(A)] + [10**20]
    t = [-10**20] + [int(input()) for _ in range(B)] + [10**20]
    x = [int(input()) for _ in range(Q)]
    for i in x:
        s_index = bisect.bisect_left(s, i)
        t_index = bisect.bisect_left(t, i)
        ans = 10**20
        for j in [s[s_index-1], s[s_index]]:
            for k in [t[t_index-1], t[t_index]]:
                ans = min(ans, max(i-j, 0) + max(k-i, 0), max(i-k, 0) + max(j-i, 0))
        print(ans)
