def main():
    import bisect
    import sys
    input = sys.stdin.readline
    A, B, Q = map(int, input().split())
    S = [-10**10] + [int(input()) for _ in range(A)] + [10**10]
    T = [-10**10] + [int(input()) for _ in range(B)] + [10**10]
    X = [int(input()) for _ in range(Q)]
    for x in X:
        i = bisect.bisect_right(S, x)
        j = bisect.bisect_right(T, x)
        ans = 10**20
        for s in S[i-1:i+1]:
            for t in T[j-1:j+1]:
                ans = min(ans, max(s-x, x-t), max(t-x, x-s))
        print(ans)
