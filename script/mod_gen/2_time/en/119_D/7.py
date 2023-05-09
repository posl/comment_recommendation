def solve():
    A, B, Q = map(int, input().split())
    S = [-10**20] + [int(input()) for _ in range(A)] + [10**20]
    T = [-10**20] + [int(input()) for _ in range(B)] + [10**20]
    X = [int(input()) for _ in range(Q)]
    ans = []
    for x in X:
        s = bisect.bisect_right(S, x)
        t = bisect.bisect_right(T, x)
        ans.append(min(
            max(S[s - 1], T[t - 1]) - x,
            x - min(S[s], T[t]),
            S[s] - T[t - 1] + min(S[s] - x, x - T[t - 1]),
            T[t] - S[s - 1] + min(T[t] - x, x - S[s - 1]),
        ))
    print('
'.join(map(str, ans)))

if __name__ == '__main__':
    solve()