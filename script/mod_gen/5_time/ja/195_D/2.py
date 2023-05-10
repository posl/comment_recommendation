def main():
    N,M,Q = map(int,input().split())
    WV = [list(map(int,input().split())) for _ in range(N)]
    X = list(map(int,input().split()))
    Query = [list(map(int,input().split())) for _ in range(Q)]
    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X_new = X[:L-1] + X[R:]
        X_new.sort()
        ans = 0
        for j in range(N):
            for k in range(len(X_new)):
                if WV[j][0] <= X_new[k]:
                    ans += WV[j][1]
                    X_new.pop(k)
                    break
        print(ans)

if __name__ == '__main__':
    main()