def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        boxes = X[:L-1] + X[R:]
        boxes.sort()
        w = []
        v = []
        for i in range(N):
            if W[i] <= boxes[-1]:
                w.append(W[i])
                v.append(V[i])
        dp = [[0]*(len(boxes)+1) for i in range(len(w)+1)]
        for i in range(len(w)):
            for j in range(len(boxes)):
                if w[i] <= boxes[j]:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i][j] + v[i])
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        print(dp[-1][-1])

if __name__ == '__main__':
    main()