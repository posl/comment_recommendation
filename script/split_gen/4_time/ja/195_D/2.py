def main():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]
    WV.sort(key=lambda x: x[1], reverse=True)
    for i in range(Q):
        l = Query[i][0]
        r = Query[i][1]
        X_ = X[:l-1] + X[r:]
        X_.sort()
        ans = 0
        for j in range(N):
            for k in range(len(X_)):
                if WV[j][0] <= X_[k]:
                    ans += WV[j][1]
                    X_.pop(k)
                    break
        print(ans)
