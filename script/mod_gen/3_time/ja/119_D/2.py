def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    S = [float('-inf')] + S + [float('inf')]
    T = [float('-inf')] + T + [float('inf')]
    from bisect import bisect_left, bisect_right
    for x in X:
        s = bisect_right(S, x)
        t = bisect_right(T, x)
        ans = float('inf')
        for s1 in [S[s-1], S[s]]:
            for t1 in [T[t-1], T[t]]:
                ans = min(ans, abs(x-s1)+abs(s1-t1), abs(x-t1)+abs(t1-s1))
        print(ans)

if __name__ == '__main__':
    main()