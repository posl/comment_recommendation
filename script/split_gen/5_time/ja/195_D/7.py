def main():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for i in range(Q):
        ans = 0
        l = Query[i][0]
        r = Query[i][1]
        box = X[:l-1] + X[r:]
        box.sort()
        for j in range(N):
            for k in range(len(box)):
                if WV[j][0] <= box[k]:
                    ans += WV[j][1]
                    del box[k]
                    break
        print(ans)
