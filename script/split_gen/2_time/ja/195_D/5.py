def main():
    N, M, Q = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        x = X[:L - 1] + X[R:]
        x.sort()
        wv.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for wi, vi in wv:
            for i, xi in enumerate(x):
                if xi >= wi:
                    ans += vi
                    x[i] = -1
                    break
        print(ans)
