def main():
    A, B, Q = map(int, input().split())
    s = [-10**12] + [int(input()) for _ in range(A)] + [10**12]
    t = [-10**12] + [int(input()) for _ in range(B)] + [10**12]
    x = [int(input()) for _ in range(Q)]
    for i in x:
        s_idx = bisect.bisect_right(s, i)
        t_idx = bisect.bisect_right(t, i)
        ans = 10**12
        for j in range(s_idx - 1, s_idx + 1):
            for k in range(t_idx - 1, t_idx + 1):
                ans = min(ans, abs(i - s[j]) + abs(s[j] - t[k]), abs(i - t[k]) + abs(t[k] - s[j]))
        print(ans)
