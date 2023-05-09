def solve():
    A, B, Q = [int(i) for i in input().split()]
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s = [-float("inf")] + s + [float("inf")]
    t = [-float("inf")] + t + [float("inf")]
    for i in x:
        s_idx = bisect_left(s, i)
        t_idx = bisect_left(t, i)
        ans = float("inf")
        for j in [s[s_idx-1], s[s_idx]]:
            for k in [t[t_idx-1], t[t_idx]]:
                if j <= i and i <= k:
                    ans = min(ans, max(i-j, k-i))
                else:
                    ans = min(ans, abs(i-j) + abs(j-k), abs(i-k) + abs(k-j))
        print(ans)
solve()

if __name__ == '__main__':
    solve()