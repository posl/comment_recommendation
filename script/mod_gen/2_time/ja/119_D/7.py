def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    from bisect import bisect_left, bisect_right
    from itertools import accumulate
    from operator import itemgetter
    INF = float('inf')
    A, B, Q = map(int, readline().split())
    S = [int(readline()) for _ in range(A)]
    T = [int(readline()) for _ in range(B)]
    X = [int(readline()) for _ in range(Q)]
    for x in X:
        s = bisect_left(S, x)
        t = bisect_left(T, x)
        res = INF
        for ss in [S[s-1], S[s]] if s > 0 else [S[s]]:
            for tt in [T[t-1], T[t]] if t > 0 else [T[t]]:
                res = min(res, abs(ss - x) + abs(ss - tt), abs(tt - x) + abs(ss - tt))
        print(res)

if __name__ == '__main__':
    main()