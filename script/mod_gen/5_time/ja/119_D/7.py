def solve():
    #入力
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    #番兵
    S = [-10**11] + S + [10**11]
    T = [-10**11] + T + [10**11]
    #二分探索
    from bisect import bisect_left, bisect_right
    for x in X:
        s = bisect_left(S, x)
        t = bisect_left(T, x)
        ans = 10**18
        for ss in [S[s-1], S[s]]:
            for tt in [T[t-1], T[t]]:
                #print(ss,tt)
                d1 = abs(ss-x) + abs(tt-ss)
                d2 = abs(tt-x) + abs(ss-tt)
                d3 = abs(ss-tt) + abs(x-tt)
                d4 = abs(tt-ss) + abs(x-ss)
                ans = min(ans, d1, d2, d3, d4)
        print(ans)

if __name__ == '__main__':
    solve()