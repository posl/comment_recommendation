def main():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    LR = [list(map(int, input().split())) for _ in range(Q)]
    WV.sort(key=lambda x: x[1], reverse=True)
    for l, r in LR:
        x = X[:l-1] + X[r:]
        x.sort()
        ans = 0
        for w, v in WV:
            for i, xi in enumerate(x):
                if w <= xi:
                    ans += v
                    x.pop(i)
                    break
        print(ans)
